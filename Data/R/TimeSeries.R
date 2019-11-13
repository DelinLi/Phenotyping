library(PerformanceAnalytics)

Data <-read.delim("../example/MiFlora.Recording.soybean.201910.txt",header = F)

Data.1<-Data[Data$Flora %in% "Flora2",]
rownames(Data.1)<-Data.1$date.time

R=Data.1[,"moisture",drop=FALSE]
charts.TimeSeries(R)
