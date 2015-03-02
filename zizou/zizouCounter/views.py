from django.shortcuts import render


DEFAULT_VALUES = {
  'firstInt': 3,
  'secondInt': 5,
  'firstString': "Zi",
  'secondString': "Zou",
  'maxValue': 100
}

def computeResults(firstInt, secondInt, firstString, secondString, maxValue):
  """Compute the results of the ZiZou experience."""
  for i in range(1, maxValue + 1):
    if i % firstInt == 0:
      if i % secondInt == 0:
        yield firstString + secondString
      else:
        yield firstString
    elif i % secondInt == 0:
      yield secondString
    else:
      yield str(i)


def index(request):
  try:
    context = {'firstInt': 3, 'secondInt': 5, 'firstString': "Zi", 'secondString': 'Zou', 'maxValue': 100}
    firstInt = int(request.POST.get('firstInt', 3))
    secondInt = int(request.POST.get('secondInt', 5))
    firstString = request.POST.get('firstString', 'Zi')
    secondString = request.POST.get('secondString', 'Zou')
    maxValue = int(request.POST.get('maxValue', 100))
    myResult = ", ".join(list(computeResults(firstInt, secondInt, firstString, secondString, maxValue)))
    context['myResult'] = myResult
  except Exception, e:
    context['error_message'] = "There was an error, the request couldn't be completed: %s" % e.message
  return render(request, 'zizouCounter/index.html', context)
