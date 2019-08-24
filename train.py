import cognitive_face as CF
from global_variables import personGroupId

Key = 'adc934ffada34e53944934fb87cd9442'
CF.Key.set(Key)
BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)
res = CF.person_group.train(personGroupId)
print (res)
