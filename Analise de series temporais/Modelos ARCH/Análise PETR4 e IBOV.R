# Pacotes
library(BatchGetSymbols)
library(rugarch)
library(tidyverse)
library(ggthemes)
library(FinTS)
library(xtable)
library(tbl2xts)

# Coleta de Dados - PETROBRAS (PETR4.SA)
tickers <- c("PETR4.SA")
dados_petr <- BatchGetSymbols(tickers = tickers,
                              first.date = as.Date('2019-01-01'),
                              last.date = Sys.Date(),
                              type.return = "log",
                              freq.data = "daily")
dados_petr <- dados_petr[[2]]

# Tratamento da Série de Retornos - PETROBRAS
retornos_petr <- dados_petr %>% 
  select(ref.date, ret.closing.prices) %>% 
  rename(date = ref.date, ret = ret.closing.prices) %>% 
  drop_na()
retornos_petr <- retornos_petr$ret

# Teste de Efeito ARCH: Teste LM
ArchTest(retornos_petr, lags = 10, demean = TRUE)

# Teste de Heterocedasticidade Condicional
ArchTest(retornos_petr, lags = 1, demean = TRUE)
ArchTest(retornos_petr, lags = 2, demean = TRUE)
ArchTest(retornos_petr, lags = 10, demean = TRUE)

# GARCH(1,1) - PETROBRAS com dist. normal e t-Student
spec_petr_norm <- ugarchspec(
  variance.model = list(model = "sGARCH", garchOrder = c(1,1)),
  mean.model = list(armaOrder = c(0,0), include.mean = FALSE),
  distribution.model = "norm")
fit_petr_norm <- ugarchfit(spec = spec_petr_norm, data = retornos_petr)

spec_petr_std <- ugarchspec(
  variance.model = list(model = "sGARCH", garchOrder = c(1,1)),
  mean.model = list(armaOrder = c(0,0), include.mean = FALSE),
  distribution.model = "std")
fit_petr_std <- ugarchfit(spec = spec_petr_std, data = retornos_petr)

# Estimando GARCH(1,1) com distribuição t-Student
spec_std <- ugarchspec(
  variance.model = list(model = "sGARCH", garchOrder = c(1,1)),
  mean.model = list(armaOrder = c(0,0), include.mean = FALSE),
  distribution.model = "std")
fit_std <- ugarchfit(spec = spec_std, data = retornos_petr)
fit_std

# Persistência e Critérios de Informação
persistence(fit_petr_norm)
persistence(fit_std)

infocriteria(fit_petr_norm)
infocriteria(fit_std)

# Volatilidade Condicional Estimada
sigma <- sigma(fit_std) %>% xts_tbl()
colnames(sigma) <- c("date", "sigma")
sigma <- sigma %>% mutate(date = as.Date(date))
ggplot(sigma) + 
  geom_line(aes(x = date, y = sigma)) + 
  theme_solarized() + 
  ggtitle("Volatilidade Condicional Estimada - PETROBRAS")

# Previsão de Volatilidade (10 passos à frente)
forecast_std <- ugarchforecast(fit_std, n.ahead = 10)
plot(forecast_std, which = 1)

# Coleta de Dados - IBOVESPA (^BVSP)
tickers_ibov <- c("^BVSP")
dados_ibov <- BatchGetSymbols(tickers = tickers_ibov,
                              first.date = as.Date('2019-01-01'),
                              last.date = Sys.Date(),
                              type.return = "log",
                              freq.data = "daily")
dados_ibov <- dados_ibov[[2]]

# Tratamento da Série de Retornos - IBOVESPA
retornos_ibov <- dados_ibov %>% 
  select(ref.date, ret.closing.prices) %>% 
  rename(date = ref.date, ret = ret.closing.prices) %>% 
  drop_na()
retornos_ibov <- retornos_ibov$ret

# Teste de Efeito ARCH - IBOVESPA
ArchTest(retornos_ibov, lags = 10, demean = TRUE)

# GARCH(1,1) - IBOVESPA com dist. normal e t-Student
spec_ibov_norm <- ugarchspec(
  variance.model = list(model = "sGARCH", garchOrder = c(1,1)),
  mean.model = list(armaOrder = c(0,0), include.mean = FALSE),
  distribution.model = "norm")
fit_ibov_norm <- ugarchfit(spec = spec_ibov_norm, data = retornos_ibov)

spec_ibov_std <- ugarchspec(
  variance.model = list(model = "sGARCH", garchOrder = c(1,1)),
  mean.model = list(armaOrder = c(0,0), include.mean = FALSE),
  distribution.model = "std")
fit_ibov_std <- ugarchfit(spec = spec_ibov_std, data = retornos_ibov)

# Cálculo da Persistência (PETROBRAS e IBOVESPA)
persist_petr_norm <- persistence(fit_petr_norm)
persist_petr_std <- persistence(fit_petr_std)
persist_ibov_norm <- persistence(fit_ibov_norm)
persist_ibov_std <- persistence(fit_ibov_std)
persist_petr_norm; persist_petr_std
persist_ibov_norm; persist_ibov_std

# Cálculo do Half-life da Volatilidade
half_life <- function(p) {-log(2)/log(p)}
half_life(persist_petr_norm)
half_life(persist_petr_std)
half_life(persist_ibov_norm)
half_life(persist_ibov_std)

# Interpretação
cat("\nInterpretação:\n")
cat("A persistência indica quanto tempo os choques permanecem influenciando a volatilidade.\n")
cat("Valores próximos de 1 indicam que os choques têm efeito duradouro.\n")
cat("O half-life mede em quantos períodos a volatilidade condicional se reduz pela metade após um choque.\n")
cat("Valores altos de persistência e half-life longos indicam que a volatilidade reage lentamente a choques.\n")
