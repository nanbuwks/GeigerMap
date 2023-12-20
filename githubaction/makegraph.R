library(ggplot2)
args <- commandArgs(trailingOnly = TRUE)
input_file <- args[1]
output_file <- args[2]
# data <- read.csv(input_file)
data <- read.table(file=input_file, sep="\t",
           header=T
           )
# data <- dplyr::mutate(data, date = as.POSIXct(date,tz="Asia/Tokyo"))
png(output_file, width = 300, height = 280)
ggplot(aes(x = data[[3]], y = data[[4]]), data = data) + geom_bar(stat="identity")  + scale_y_continuous(expand = c(0, 0), limits = c(0, max(data[[4]])*1.1)) + xlab("")+ylab("μSv/h")
dev.off() 
