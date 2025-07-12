knitr::opts_chunk$set(echo = TRUE)


library(BatchGetSymbols)
library(rugarch)
library(tidyverse)
library(ggthemes)
library(FinTS)
library(xtable)
library(tbl2xts)


tickers_vale <- c("VALE3.SA")
dados_vale <- BatchGetSymbols(tickers = tickers_vale,
                              first.date = as.Date('2019-01-01'),
                              last.date = Sys.Date(),
                              type.return = "log",
                              freq.data = "daily")
dados_vale <- dados_vale[[2]]


retornos_vale <- dados_vale %>% 
  select(ref.date, ret.closing.prices) %>% 
  rename(date = ref.date, ret = ret.closing.prices) %>% 
  drop_na()
retornos_vale <- retornos_vale$ret


ArchTest(retornos_vale, lags = 10, demean = TRUE)


modelos <- list(
  garch_norm = ugarchspec(variance.model = list(model = "sGARCH", garchOrder = c(1,1)),
                          mean.model = list(armaOrder = c(0,0), include.mean = FALSE),
                          distribution.model = "norm"),
  garch_std = ugarchspec(variance.model = list(model = "sGARCH", garchOrder = c(1,1)),
                         mean.model = list(armaOrder = c(0,0), include.mean = FALSE),
                         distribution.model = "std"),
  egarch_norm = ugarchspec(variance.model = list(model = "eGARCH", garchOrder = c(1,1)),
                           mean.model = list(armaOrder = c(0,0), include.mean = FALSE),
                           distribution.model = "norm"),
  egarch_std = ugarchspec(variance.model = list(model = "eGARCH", garchOrder = c(1,1)),
                          mean.model = list(armaOrder = c(0,0), include.mean = FALSE),
                          distribution.model = "std"),
  gjr_norm = ugarchspec(variance.model = list(model = "gjrGARCH", garchOrder = c(1,1)),
                        mean.model = list(armaOrder = c(0,0), include.mean = FALSE),
                        distribution.model = "norm"),
  gjr_std = ugarchspec(variance.model = list(model = "gjrGARCH", garchOrder = c(1,1)),
                       mean.model = list(armaOrder = c(0,0), include.mean = FALSE),
                       distribution.model = "std")
)



ajustes <- lapply(modelos, function(spec) {
  try(ugarchfit(spec = spec, data = retornos_vale), silent = TRUE)
})



ajustes_validos <- ajustes[!sapply(ajustes, inherits, "try-error")]

criterios <- sapply(ajustes_validos, infocriteria)

if (is.null(rownames(criterios))) {
  rownames(criterios) <- c("Akaike", "Bayes", "Shibata", "Hannan-Quinn")
}

print(round(criterios, 4))



melhor_modelo_nome <- colnames(criterios)[which.min(criterios["Akaike", ])]
melhor_ajuste <- ajustes_validos[[melhor_modelo_nome]]
cat("Melhor modelo com base no AIC:", melhor_modelo_nome)


plot(melhor_ajuste, which = "all")


previsao <- ugarchforecast(melhor_ajuste, n.ahead = 10)
plot(previsao, which = 1)
