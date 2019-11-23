setwd("~/Documents/github/Phenotyping/Data/")
library(PerformanceAnalytics)

Data <-read.delim("example/Miflora.Recording.2019.Home.txt",header = T)


Rainy<-c("2019-09-09/2019-09-13","2019-10-03/2019-10-04","2019-10-12/2019-10-13")
Start.points<-c("2019-09-08","2019-09-12","2019-10-02","2019-10-03","2019-10-12","2019-10-11") # addressing line shiftted 
###1. Plot for Temp
Temp <- cbind(Data[ Data$Flora %in% "Out" ,c("Time","Temp")],Data$Temp[ Data$Flora %in% "In" ] )

colnames(Temp) <- c("Time","Sand","Soil")
Temp<-Temp[grep("14:00",Temp$Time),]
rownames(Temp)<-sub(" .*","",Temp$Time)
R=Temp[,c("Soil","Sand"), drop = FALSE]

pdf("figures/outdoor.Temp.Rep.pdf",width = 9,height = 7)
chart.TimeSeries(R,main="",legend.loc="topright",ylab = "Temp.",
                 period.color = rgb(204/255, 204/255, 204/255, alpha=0.4),
                 period.areas = Rainy,
                 event.lines = Start.points,
                 event.color ="white",
                 event.labels = rep("",length(Start.points)),
                 date.format="%Y-%m-%d",cex.legend = 1.2)
dev.off()
###2. Plot for "moisture"
moisture <- cbind(Data[ Data$Flora %in% "Out" ,c("Time","moisture")],Data$moisture[ Data$Flora %in% "In" ] )

colnames(moisture) <- c("Time","Sand","Soil")
moisture<-moisture[grep("12:00",moisture$Time),]
rownames(moisture)<-sub(" .*","",moisture$Time)
R=moisture[,c("Soil","Sand"), drop = FALSE]

pdf("figures/outdoor.different.Soil.moisture.pdf",width = 9,height = 7)

chart.TimeSeries(R,main="",legend.loc="topright",ylab = "moisture.",
                 period.color = rgb(204/255, 204/255, 204/255, alpha=0.25),
                 period.areas = Rainy,
                 event.lines = Start.points,
                 event.labels = rep("",length(Start.points)),
                 date.format="%Y-%m-%d" ,cex.legend = 1.2 )
 dev.off()


###3. Plot for ""
conductivity <- cbind(Data[ Data$Flora %in% "Out" ,c("Time","conductivity")],Data$conductivity[ Data$Flora %in% "In" ] )

colnames(conductivity) <- c("Time","Sand","Soil")
conductivity<-conductivity[grep("14:00",conductivity$Time),]
rownames(conductivity)<-sub(" .*","",conductivity$Time)
R=conductivity[,c("Soil","Sand"), drop = FALSE]

pdf("figures/Different.Soil.conductivity.pdf",width = 9,height = 7)

chart.TimeSeries(R,main="",legend.loc="topright",ylab = "conductivity",
                 period.color = rgb(204/255, 204/255, 204/255, alpha=0.25),
                 period.areas = Rainy,
                 event.lines = Start.points,
                 event.labels = rep("",length(Start.points)),
                 date.format="%Y-%m-%d",cex.legend = 1.2 )
 
dev.off()

###3. Plot for ""
#green house, light controled 

pdf("figures/PhytotronLightDsitribution.pdf",width = 7,height = 9)
par(mfrow=c(2,1))
hist( Data$light[Data$Flora %in% "In"],main="Outdoor Light Dsitribution (every 10 min)",
     xlab=" Light Evaluted by Mi-Flora",cex.lab=1.4) #  light pollution
Data.GH <-read.delim("example/MiFlora.Recording.soybean.201910.txt",header = T)
hist(Data.GH$light[Data.GH$Flora %in% "Flora1"],main="Phytotron Light Dsitribution (every 10 min)",
     xlab="Light Evaluted by Mi-Flora",cex.lab=1.4)
dev.off()

pdf("figures/PhytotronLightDsitribution.log10.pdf",width = 7,height = 9)
par(mfrow=c(2,1))
hist(log10(Data$light[Data$Flora %in% "In"]),main="Outdoor Light Dsitribution (every 10 min)",
     xlab="log10(Light) Evaluted by Mi-Flora",cex.lab=1.4) #  light pollution
Data.GH <-read.delim("example/MiFlora.Recording.soybean.201910.txt",header = T)
hist(log10(Data.GH$light[Data.GH$Flora %in% "Flora1"]),main="Phytotron Light Dsitribution (every 10 min)",
     xlab="log10(Light) Evaluted by Mi-Flora",cex.lab=1.4)
dev.off()

 