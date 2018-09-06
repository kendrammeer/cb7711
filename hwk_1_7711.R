#If ggplot2 package is not installed on your are (error with library(ggplot2) command), run comment below to install the package
#install.packages("ggplot2")

#Import ggplot2 from the package library
library(ggplot2)

#Initiate the values for the x-axis, True negative values 5->100
TN <- seq(5,100,1)

#Create a data frame from these x-values
df <- data.frame(TN)

#Add TP,FP,FN rows to the data frame with set values of 5
df$TP <- rep(5,nrow(df))
df$FP <- rep(5,nrow(df))
df$FN <- rep(5,nrow(df))

#Precision and recall functions
precision <- function(TP,FP){
  TP/(TP+FP)
}

recall <- function(TP,FN){
  TP/(TP+FN)
}

#Create list of precision and recall values for input into f-score function
pre <- precision(df$TP,df$FP)

re <- recall(df$TP,df$FN)

#Functions for F-score and Accuracy 
fscore <- function(pre,re){
  2*((pre*re)/(pre+re))
}

accuracy <- function(TN,TP,FN,FP){
  (TP+TN)/(TP+TN+FP+FN)
}

#Calculate F-score and Accuracy for each value of TN and add to dataframe (F-score should not change since recall and precision don't change)
df$fscore <- fscore(pre,re)
df$accuracy <- accuracy(df$TN,df$TP,df$FN,df$FP)

#Plot F-score and accuracy
p <- ggplot()+geom_point(data=df,aes(x=df$TN,y=df$fscore,shape="F-score"),size=3)+
  geom_point(data=df,aes(x=df$TN,y=df$accuracy,shape="Accuracy"),size=3)+
  scale_shape_manual(values=c(17,16))+theme_classic()

p_final<-p + labs(y='', x="True Negatives")+ theme(legend.title = element_blank())

p_final

#Save plot as png file
png("Accuracy_Fscore_Plot.png")
p_final
dev.off()