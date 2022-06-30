import numpy as np

def calculate(list):
  if len(list)<9:
    raise ValueError("List must contain nine numbers.")
  
  listlist = np.array(list).reshape((3,3))

  listlistSum = listlist.sum().tolist()
  listlistMean = listlist.mean().tolist()
  listlistMax = listlist.max().tolist()
  listlistMin = listlist.min().tolist()
  listlistStdDeviation = listlist.std().tolist()
  listlistVariance = listlist.var().tolist()

  listlistSumAxis1 = listlist.sum(axis=1).tolist()
  listlistMeanAxis1 = listlist.mean(axis=1).tolist()
  listlistMaxAxis1 = listlist.max(axis=1).tolist()
  listlistMinAxis1 = listlist.min(axis=1).tolist()
  listlistStdDeviationAxis1 = listlist.std(axis=1).tolist()
  listlistVarianceAxis1 = listlist.var(axis=1).tolist()

  listlistSumAxis0 = listlist.sum(axis=0).tolist()
  listlistMeanAxis0 = listlist.mean(axis=0).tolist()
  listlistMaxAxis0 = listlist.max(axis=0).tolist()
  listlistMinAxis0 = listlist.min(axis=0).tolist()
  listlistStdDeviationAxis0 = listlist.std(axis=0).tolist()
  listlistVarianceAxis0 = listlist.var(axis=0).tolist()

  return  {
  'mean': [listlistMeanAxis0,listlistMeanAxis1,listlistMean],
  'variance': [listlistVarianceAxis0,listlistVarianceAxis1,listlistVariance],
  'standard deviation': [listlistStdDeviationAxis0,listlistStdDeviationAxis1,listlistStdDeviation],
  'max': [listlistMaxAxis0,listlistMaxAxis1,listlistMax],
  'min': [listlistMinAxis0,listlistMinAxis1,listlistMin],
  'sum': [listlistSumAxis0,listlistSumAxis1,listlistSum]
}

calculate([0,1,2,3,4,5,6,7,8])