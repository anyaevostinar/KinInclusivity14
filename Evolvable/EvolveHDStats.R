require(ggplot2)

setwd("~/Dropbox/Vital2/MSU/ExclusivityPaper")

### Calculating evolvable HD
evolve_hd <- read.table("munged_avg_hd.dat", h=T)
medpop_lowmut <- subset(evolve_hd, treatment=="5k-0002")
medpop_lowmut <- cbind(medpop_lowmut, Population="5000", Mutation = "0.02")
medpop_medmut <- subset(evolve_hd, treatment=="5k-002")
medpop_medmut <- cbind(medpop_medmut, Population="5000", Mutation = "0.2")
medpop_highmut <- subset(evolve_hd, treatment=="5k-02")
medpop_highmut <- cbind(medpop_highmut, Population="5000", Mutation = "2.0")

bigpop_medmut <- subset(evolve_hd, treatment=="10k-002")
bigpop_medmut <- cbind(bigpop_medmut, Population="10000", Mutation = "0.2")
bigpop_lowmut <- subset(evolve_hd, treatment=="10k-0002")
bigpop_lowmut <- cbind(bigpop_lowmut, Population="10000", Mutation = "0.02")
bigpop_highmut <- subset(evolve_hd, treatment=="10k-02")
bigpop_highmut <- cbind(bigpop_highmut, Population="10000", Mutation = "2.0")

smallpop_medmut <-subset(evolve_hd, treatment=="1k-002")
smallpop_medmut <- cbind(smallpop_medmut, Population="1000", Mutation = "0.2")
smallpop_lowmut <- subset(evolve_hd, treatment=="1k-0002")
smallpop_lowmut <- cbind(smallpop_lowmut, Population="1000", Mutation = "0.02")
smallpop_highmut <- subset(evolve_hd, treatment=="1k-02")
smallpop_highmut <- cbind(smallpop_highmut, Population="1000", Mutation = "2.0")

median(smallpop_highmut$avg_hd)
median(medpop_highmut$avg_hd)
median(bigpop_highmut$avg_hd)

median(smallpop_medmut$avg_hd)
median(medpop_medmut$avg_hd)
median(bigpop_medmut$avg_hd)

median(smallpop_lowmut$avg_hd)
median(medpop_lowmut$avg_hd)
median(bigpop_lowmut$avg_hd)

full_data <- rbind(smallpop_highmut, smallpop_medmut, smallpop_lowmut,medpop_highmut, medpop_medmut, medpop_lowmut,bigpop_highmut, bigpop_medmut, bigpop_lowmut)

ggplot(data=full_data, aes(x=1, y=avg_hd)) + ylab("Average Evolved Hamming Distance \n Mutation Rate") + xlab("Population Size") + geom_boxplot(width=0.5, aes(fill=treatment)) + theme(panel.background = element_rect(fill='white', colour='black')) + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank()) + guides(fill=FALSE) + facet_wrap(~Mutation*Population) +theme(strip.background = element_blank(),strip.text.x = element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank())
