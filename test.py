import pickle

questions=pickle.load( open( "questions.pckl", "rb" ) )
for s in questions.keys():
    print(s+": "+str(questions[s]))