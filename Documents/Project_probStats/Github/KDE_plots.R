# to plot kde 
plot_kde=function(x,a,b){
par(mfrow=c(3, 3))
colnames <- dimnames(x)[[2]] #insert dataframe in place of corr_state_level
for (i in a:b) {  #specify the range of numeric columns you want to plot.
d <- density(x[,i])#insert your dataframe in place of corr_state_level
plot(d, type="n", main=colnames[i])
polygon(d, col="red", border="gray")
}}