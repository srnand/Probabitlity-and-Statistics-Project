ks=function(x){
  normal_theory=rnorm(length(x),mean(x,na.rm = TRUE),sd(x,na.rm = TRUE))
  
  ks.test(x,normal_theory)
}
