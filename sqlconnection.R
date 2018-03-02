library(RODBC)
# 
# dbhandle <- odbcDriverConnect('driver={SQL Server};server=WINNYRPDB01;database=allocations;trusted_connection=true')
# res <- sqlQuery(dbhandle, 
# "SELECT
# 
# from AllocableUsers 
# where startDate is not null  
# order by startDate")


#rw <- readRDS("C:\\Users\\varunn\\Documents\\kaggle competiton\\healthexp.Rds")







library(xlsx)
setwd("~/kaggle competiton")
Data <- read.xlsx("DeptAnalysis.xlsx", sheetIndex = 1)
#install.packages("plyr")
library(plyr)
agg  <- ddply(Data,.(Department,Office,Year,Mth),nrow)
agg$Office <- as.factor(agg$Office)
agg <- agg[,c(2,1,3,4,5)]
agg$pop <- agg$V1



