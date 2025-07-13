# Importação de Pacotes
library(BatchGetSymbols)
library(tidyverse)
library(forecast)
library(tseries)
library(FinTS)
library(xts)
library(dplyr)
library(tibble)
library(lubridate)
library(tidyr)

# Análise visual da série
tickers <- c("^BVSP")

ibov_data <- BatchGetSymbols(tickers = tickers,
                             first.date = as.Date("2021-01-01"),
                             last.date = Sys.Date(),
                             type.return = "log",
                             freq.data = "daily")

ibov <- ibov_data[[2]]

retornos <- ibov %>%
  select(ref.date, ret.closing.prices) %>%
  drop_na()

retornos_ts <- ts(retornos$ret.closing.prices)

plot(retornos_ts, main = "Retornos Diários do IBOVESPA", col = "darkblue", ylab = "Retornos", xlab = "Tempo")

# Indentificação do modelo
# Correlograma da série
acf(retornos_ts, lag.max = 36, main = "FAC - Retornos IBOVESPA")
pacf(retornos_ts, lag.max = 36, main = "FACP - Retornos IBOVESPA")

forecast::tsdisplay(retornos_ts, lag.max = 36, main = "Identificação via tsdisplay")

#  Estimação do modelo
# Exemplo: ARMA(1,1)
modelo_arma <- arima(retornos_ts, order = c(1, 0, 1))

summary(modelo_arma)

AIC(modelo_arma)
BIC(modelo_arma)

modelo_auto <- auto.arima(retornos_ts, seasonal = FALSE)
summary(modelo_auto)


# Diagnóstico dos resíduos 
plot.ts(modelo_arma$residuals, main = "Resíduos do Modelo ARMA(1,1)", col = "gray")

acf(residuals(modelo_arma), main = "FAC dos Resíduos")
pacf(residuals(modelo_arma), main = "FACP dos Resíduos")

# Testes Ljung-Box e Box-Pierce
Box.test(residuals(modelo_arma), lag = 10, type = "Ljung")
Box.test(residuals(modelo_arma), lag = 10, type = "Box-Pierce")

# Comparação: valores observados vs ajustados
plot(retornos_ts, col = "red", main = "Observado (vermelho) vs Ajustado (azul)", ylab = "Retornos", xlab = "Tempo")
lines(fitted(modelo_arma), col = "blue")

# Previsão para 5 períodos
previsao <- forecast::forecast(modelo_arma, h = 5)

previsao_df <- data.frame(
  Previsao = round(previsao$mean, 6),
  IC_Inferior = round(previsao$lower[,2], 6),
  IC_Superior = round(previsao$upper[,2], 6)
)
rownames(previsao_df) <- paste0("t+", 1:5)
previsao_df

plot(previsao, main = "Previsão de Retornos - Modelo ARMA", xlab = "Tempo", ylab = "Retornos")

# Modelo ARMA para ações S&P500
# Selecionando top empresas do S&P500
tickers <- c("AAPL", "MSFT", "GOOG", "AMZN", "META", "TSLA", "NVDA", "JPM", "UNH", "V")

first_date <- as.Date("2021-01-01")
last_date <- Sys.Date()

pegar_dados_seguro <- function(tkr) {
  tryCatch({
    BatchGetSymbols(tickers = tkr,
                    first.date = first_date,
                    last.date = last_date,
                    type.return = "log",
                    freq.data = "daily",
                    thresh.bad.data = 0.9,
                    do.cache = FALSE)[[2]]
  }, error = function(e) {
    message(paste("Erro com", tkr, ":", e$message))
    return(NULL)
  })
}

lista_dados <- lapply(tickers, pegar_dados_seguro)
lista_dados_validos <- Filter(function(x) !is.null(x) && nrow(x) > 0, lista_dados)

# Unindo todos os dados em um dataframe
dados <- bind_rows(lista_dados_validos)

dados_validos <- dados %>%
  filter(!is.na(ret.closing.prices)) %>%
  group_by(ticker) %>%
  filter(n() >= 30) %>%  # Mínimo de 30 observações
  ungroup()

# Estimando ARMA(1,1) e prevendo retorno t+1
arma_por_acao <- dados_validos %>%
  group_by(ticker) %>%
  summarise(previsao_t1 = {
    ts_data <- ts(ret.closing.prices)
    modelo <- tryCatch(arima(ts_data, order = c(1, 0, 1)), error = function(e) NULL)
    if (!is.null(modelo)) {
      as.numeric(forecast(modelo, h = 1)$mean[1])
    } else {
      NA
    }
  }, .groups = "drop") %>%
  filter(!is.na(previsao_t1)) %>%
  arrange(desc(previsao_t1))

head(arma_por_acao, 10)
melhor_acao <- arma_por_acao %>% slice(1)
melhor_acao

#  Separação de dados do S&P500 para comparação
simular_estrategia <- function(retornos, janela_estima = 60) {
  
  n <- length(retornos)
  retornos_estrategia <- rep(NA, n)
  
  for (t in (janela_estima + 1):(n - 1)) {
    
    y_estima <- retornos[(t - janela_estima):(t - 1)]
    
    modelo <- tryCatch(arima(y_estima, order = c(1, 0, 1)), error = function(e) NULL)
    
    if (!is.null(modelo)) {
      pred <- forecast(modelo, h = 1)
      previsao_t1 <- as.numeric(pred$mean[1])
      
      if (previsao_t1 > 0) {
        retornos_estrategia[t + 1] <- retornos[t + 1]  
      } else {
        retornos_estrategia[t + 1] <- 0 
      }
    }
  }
  
  return(retornos_estrategia)
}

# Aplicando estratégia em uma ação (AAPL)
retornos_aapl <- dados %>%
  filter(ticker == "AAPL") %>%
  arrange(ref.date) %>%
  pull(ret.closing.prices)

retornos_estrategia <- simular_estrategia(retornos_aapl)
retornos_estrategia_ts <- ts(retornos_estrategia)

# Comparando retorno acumulado vs buy & hold
ret_acum_estrategia <- cumsum(na.omit(retornos_estrategia))
ret_acum_buyhold <- cumsum(na.omit(retornos_aapl))

plot(ret_acum_buyhold, type = "l", col = "gray", ylab = "Retorno Acumulado", main = "Estratégia ARMA vs Buy & Hold")
lines(ret_acum_estrategia, col = "blue")
legend("topleft", legend = c("Buy & Hold", "Estratégia ARMA"), col = c("gray", "blue"), lty = 1)

# Avaliação de lucro
mean_ret_arma <- mean(na.omit(retornos_estrategia))
mean_ret_buyhold <- mean(na.omit(retornos_aapl))

cat("Média de retorno (Estratégia ARMA):", round(mean_ret_arma * 100, 3), "%\n")
cat("Média de retorno (Buy & Hold):", round(mean_ret_buyhold * 100, 3), "%\n")