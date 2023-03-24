#with the help of pickle 

with open('reg.pickle', 'wb') as f: 
    pickle.dump(reg, f)

with open('reg.pickle', 'rb') as f:
    mp = pickle.load(f)
    
#with the help of joblib 

joblib.dump(reg, 'reg_joblib')
joblib.load('model_joblib')
    
    
