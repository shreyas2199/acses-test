import rasa
from rasa.nlu.model import Metadata,Interpreter
interpreter=Interpreter.load('./models/alexa-model/nlu') #time stamp changes on tarining the model
def classify_intent():

    result = interpreter.parse("""
    I want to cancel my order""")

    clf_confidence = result["intent"]["confidence"]
    clf_name = result["intent"]["name"]
    clf_response = result["response_selector"]["default"]["response"]["name"]
    print ("confidence: ",clf_confidence, "\nintent: ",clf_name, "\nresponse_id: ",clf_response)

classify_intent()