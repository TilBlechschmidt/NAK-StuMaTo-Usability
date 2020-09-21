import csv
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import average



def readProblems(path):
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

def extractAttributePerCriterion(criteria,attribute):
    result={}
    listOfCriteriaToWeightsMaps=[{criterion:[problem[attribute]for problem in problems]} for criterion,problems in criteria.items()]
    for criterion in listOfCriteriaToWeightsMaps:
        for c,weights in criterion.items():
            result[c]=weights
    return result

def distinctCountPerCriterion(criterionToAttributeList,defaults):
    result={}
    for c,ws in criterionToAttributeList.items():
        result[c]=dict(defaults)
        for w in ws:
            result[c][int(w)]+=1
    return result


def generateStackedBarChart():
    path ="C:/Development/Uni/NAK-StuMaTo-Usability/src/resources/auswertung-heur-expanded.csv"
    problems=readProblems(path)
    criteria = groupProblemsByCriteria(problems)
    weights = extractAttributePerCriterion(criteria,"weight")
    distinctWeightCount=distinctCountPerCriterion(weights,{0:0,1:0,2:0,3:0})

    labels=[]
    weightFrequencies=[[],[],[],[]]

    for criterion,weightCounts in distinctWeightCount.items():
        labels.append(criterion)
        for weight,count in weightCounts.items():
            weightFrequencies[weight].append(count)

    weightFrequencies=[np.array(x) for x in weightFrequencies]

    ind=np.arange(13)
    width=0.5

    bars=[0,0,0,0]
    bars[0]=plt.bar(ind,weightFrequencies[0],width)
    for i in range(1,4): 
        bars[i]=plt.bar(ind,weightFrequencies[i],width,bottom=sum([weightFrequencies[x] for x in range(1,i)]))

    plt.title("Gewichtungshäufigkeit je Kategorie")
    plt.ylabel('Häufigkeit')

    plt.xticks(ind,labels,rotation="vertical")
    plt.yticks(np.arange(0,15,1))
    plt.legend(bars,[0,1,2,3])
    plt.tight_layout()
    plt.savefig("../images/stacked-bar.pdf",dpi=1200)

def avg(seq):
    return float(sum(seq))/len(seq)

def generateBarChartDev():
    path ="C:/Development/Uni/NAK-StuMaTo-Usability/src/resources/auswertung-heur-expanded.csv"
    problems=readProblems(path)
    criteria = groupProblemsByCriteria(problems)
    criteriaDevs=[avg([int(p["dev"]) for p in ps]) for _, ps in criteria.items()]

    ind=np.arange(13)
    width=0.5

    plt.bar(ind,criteriaDevs,width)

    plt.title("Durchschnittswert von $\Delta$")
    plt.ylabel('$\Delta$')
    
    plt.xticks(ind,criteria.keys(),rotation="vertical")
    plt.yticks(np.arange(0,3,0.5))
    plt.tight_layout()
    plt.savefig("../images/bar-dev.pdf",dpi=1200)


def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

def generatePieChart():
    path="C:/Development/Uni/NAK-StuMaTo-Usability/src/resources/auswertung-heur.csv"
    problems=readProblems(path)
    
    labels = [3,2,1]
    weights = [problem["weight"] for problem in problems]
    
    weightCounts = [len([x for x in weights if int(x) == number]) for number in labels]

    fig1,ax1 = plt.subplots()
    ax1.pie(weightCounts,labels=labels,autopct=make_autopct(weightCounts),shadow=True,startangle=90)
    ax1.axis('equal')
    plt.savefig("../images/pie.pdf",dpi=1200)

plt.style.use('seaborn-dark')
generateBarChartDev()