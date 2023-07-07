df['job_state']=df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts()