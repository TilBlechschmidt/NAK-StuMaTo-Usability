import csv
import numpy as np
import matplotlib.pyplot as plt
path ="C:/Development/Uni/NAK-StuMaTo-Usability/src/resources/auswertung-heur.csv"


def readProblems():
    problems=[]
    with open(path) as file:
        reader=csv.reader(file,delimiter=';')
        for row in reader:
            problems.append({"id":row[0],"criterion":row[1],"weight":row[2],"dev":row[3]})
    return problems

def groupProblemsByCriteria(problems):
    criteria = {}
    for problem in problems:
        if problem["criterion"] in criteria:
            criteria[problem["criterion"]].append(problem)
        else:
            criteria[problem["criterion"]]=[problem]
    return criteria

def extractWeightsPerCriterion(criteria):
    result={}
    listOfCriteriaToWeightsMaps=[{criterion:[problem["weight"]for problem in problems]} for criterion,problems in criteria.items()]
    for criterion in listOfCriteriaToWeightsMaps:
        for c,weights in criterion.items():
            result[c]=weights
    return result

def distinctWeightCountPerCriterion(weights):
    result={}
    for c,ws in weights.items():
        result[c]={0:0,1:0,2:0,3:0}
        for w in ws:
            result[c][int(w)]+=1
    return result


            

problems=readProblems()
criteria = groupProblemsByCriteria(problems)
weights = extractWeightsPerCriterion(criteria)
distinctWeightCount=distinctWeightCountPerCriterion(weights)

labels=[]
weightFrequencies=[[],[],[],[]]

for criterion,weightCounts in distinctWeightCount.items():
    labels.append(criterion)
    for weight,count in weightCounts.items():
        weightFrequencies[weight].append(count)

weightFrequencies=[np.array(x) for x in weightFrequencies]

ind=np.arange(13)
width=0.5


plt.bar(ind,weightFrequencies[0],width)
for i in range(1,4): 
    plt.bar(ind,weightFrequencies[i],width,bottom=sum([weightFrequencies[x] for x in range(1,i)]))

plt.title("Gewichtungshäufigkeit je Kategorie")
plt.ylabel('Häufigkeit')

plt.xticks(ind,labels,rotation="vertical")
plt.yticks(np.arange(0,15,1))
plt.legend(bars,[0,1,2,3])
plt.tight_layout()
plt.savefig("./src/images/stacked-bar.pdf",dpi=1200)