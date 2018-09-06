
#Initiate the values for the x-axis, True negative values 5->100
TN <- seq(5,100,1)

#Create a data frame from these x-values
df <- data.frame(TN)


precision <- function(TP,FP){
  TP/(TP+FP)
}

recall <- function(TP,FN){
  TP/(TP+FN)
}

fscore <- function(pre,re){
  2*((pre*re)/(pre+re))
}

accuracy <- function(TN,TP,FN,FP){
  (TP+TN)/(TP+TN+FP+FN)
}


