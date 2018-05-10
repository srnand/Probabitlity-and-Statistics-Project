abbre=read.csv("C:\\Academics\\Spring2018\\CSE544 PROBS and STATS\\Project_cleaned_data\\us_states.csv")
crime=read.csv("C:\\Users\\Porkaparty\\Downloads\\crime_data_w_population_and_crime_rate.csv",stringsAsFactors = FALSE)
census16=read.csv("C:\\Academics\\Spring2018\\CSE544 PROBS and STATS\\usa-2016-presidential-election-by-county.csv",stringsAsFactors = FALSE)
yo=0;
crime[1,25]="MO"
for (i in 1:length(crime$county_name))
   {
       temp=strsplit(as.character(crime$county_name[i]),", ")
        crime$state[i]=temp[[1]][2]
         crime$county_name[i]=as.character(temp[[1]][1])
       }

for (i in 1:length(census16$County))
{
  temp=strsplit(as.character(census16$County[i]),",")
  #crime$state[i]=temp[[1]][2]
 census16$county_name[i]=as.character(temp[[1]][1])
}

combined=data.frame(median=double(),white=double(),african=double(),native=double(),asian=double(),other=double(),latino=double(),under_high_school=double(),atleast_high_school=double(),at_least_bachelors_degree=double(),graduate=double(),school=double())

for (i in 1:length(crime$county_name))
{
  for ( j in 1:length(census16$State))
  {
  if( tolower(crime$state[i])==tolower(( census16$ST[j])) && tolower(crime$county_name[i])==tolower(census16$county_name[j]))
  {
    combined$county[i]=crime$county_name[i]
    combined$state[i]=crime$state[i]
    combined$median[i]=census16[j,24]
    combined$white[i]=census16[j,25]
    combined$african[i]=census16[j,26]
    combined$native[i]=census16[j,27]
    combined$asian[i]=census16[j,28]
    combined$other[i]=census16[j,29]
    combined$latino[i]=census16[j,30]
    combined$under_high_school[i]=census16[j,19]
    combined$atleast_high_school[i]=census16[j,20]
    combined$at_least_bachelors_degree[i]=census16[j,21]
    combined$graduate[i]=census16[j,22]
    combined$school[i]=census16[j,23]
    print("yolo")
  }
  }
  
  
}
# 

count=0
for (i in 1:length(combined$county))
{
  for ( j in 1:length(census16$State))
    
  {
    if(tolower(combined$county[i])==tolower(census16$county_name[j]) && combined$white[i]==census16$White..Not.Latino..Population[j])
      count=count+1
    
  }
}