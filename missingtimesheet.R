library(FactoMineR)

Rawdata <- read.csv("C:\\Users\\varunn\\Documents\\Confluence attachments\\Finance service research\\MCA\\allbank.csv",header=T)

#check if data type is factor
str(Rawdata,list.len=ncol(Rawdata))

#covert non factor columns to factor
Rawdata[,'q50r4'] <- as.factor(Rawdata[,'q50r4'])

#identify quantitative supplimentary and qualitative supplimentary variables
res.mca <- MCA(Rawdata,quali.sup=1:12,ncp=Inf)

#execute the MCA algorithm
#res.mca <- MCA(Rawdata,quanti.sup=131,quali.sup=132:140)
#res <- MCA(data,quanti.sup=8,quali.sup=7,ncp=Inf)



plot(res.mca,invisible=c("ind"),cex=.8,autoLab = "y",selectMod = "cos2 20")
plot(res.mca,invisible=c("quanti.sup","quali.sup"),cex=.8,autoLab = "y",selectMod = "cos2 20")
plot(res.mca,label = c("var","ind"),cex=.8,autoLab = "y",selectMod = "contrib 30")

summary(res.mca,nbelements = Inf,ncp=50,file="MCAresults.txt")
summary(res.mca,nbelements = Inf,file="MCAresults.txt")

dimdesc(res.mca,axes=1:10)

res.mca$eig

res.mca <- MCA(Rawdata,quali.sup=1:12,ncp=59)

#hirarchical ascedant clustering
res.hcpc <- HCPC(res.mca,kk=Inf,min=3,max=59,consol = TRUE)

plot(res.hcpc,axes=3:4)
names(res.hcpc)
res.hcpc$call$t
res.hcpc$data.clust
res.hcpc$desc.var
res.hcpc$desc.axes
plot(res.hcpc,axes=c(1 ,2))
res.hcpc$desc.ind
write.infile(dimdesc(res.mca,axes=1:10),file="C:\\Users\\varunn\\Documents\\Confluence attachments\\Finance service research\\dimresults.csv",sep = ';',append=FALSE,nb.dec=4)
write.infile(res.mca,file="C:\\Users\\varunn\\Documents\\Confluence attachments\\Finance service research\\allbankmcaresults.csv",sep = ';',append=FALSE,nb.dec=4)
write.infile(res.hcpc$data.clust,file="C:\\Users\\varunn\\Documents\\Confluence attachments\\Finance service research\\clusterdata.csv",sep = ';',append=FALSE,nb.dec=4)
