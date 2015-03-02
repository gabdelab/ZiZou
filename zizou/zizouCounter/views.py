from django.shortcuts import render


DEFAULT_VALUES = {
  'firstInt': 3,
  'secondInt': 5,
  'firstString': "Zi",
  'secondString': "Zou",
  'maxValue': 100
}


def getCurrentValue(piValue, piFirstInt, piSecondInt, psFirstString, psSecondString):
  if piValue % piFirstInt == 0:
    if piValue % piSecondInt == 0:
      return psFirstString + psSecondString
    return psFirstString
  if piValue % piSecondInt == 0:
    return psSecondString
  return str(piValue)


def computeResults(piFirstInt, piSecondInt, psFirstString, psSecondString, piMaxValue):
  """Compute the results of the ZiZou experience.

  Args:
    - piFirstInt: first integer, used with psFirstString.
    - piSecondInt: second integer, used with psSecondString.
    - piMaxValue: maximum value.
  """
  llResults = []
  for i in range(1, piMaxValue + 1):
    llResults.append(getCurrentValue(i, piFirstInt, piSecondInt, psFirstString, psSecondString))
  return ", ".join(llResults)


def index(request):
  try:
    context = DEFAULT_VALUES
    firstInt = int(request.POST.get('firstInt', DEFAULT_VALUES['firstInt']))
    secondInt = int(request.POST.get('secondInt', DEFAULT_VALUES['secondInt']))
    firstString = request.POST.get('firstString', DEFAULT_VALUES['firstString'])
    secondString = request.POST.get('secondString', DEFAULT_VALUES['secondString'])
    maxValue = int(request.POST.get('maxValue', DEFAULT_VALUES['maxValue']))
    context['myResult'] = computeResults(firstInt, secondInt, firstString, secondString, maxValue)
  except Exception, e:
    context['error_message'] = "There was an error, the request couldn't be completed: %s" % e.message
  return render(request, 'zizouCounter/index.html', context)
