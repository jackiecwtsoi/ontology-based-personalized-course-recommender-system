'''
This is the layer where we generate career-related recommendations for a particular student.
'''

import pandas as pd
import logging
import joblib
from gensim.models.doc2vec import Doc2Vec

from ontology_profiles.student_profile.Student import *
from ontology_profiles.student_profile.PersonalInfo import *
from ontology_profiles.student_profile.EducationalInfo import *


from helper_functions import *
from generate_course_similarity import *
from configs import *

'''
FUNCTION
- Generate top k CAREER recommendations for the particular student
Return: DATAFRAME of top k recommendations (job title)
'''
def generate_career_recommendations(student: Student, CAREER_BASE_DATA_PATH, CAREER_MODEL_PATHS_DICT, k=5):
    # get the necessary student information text
    student_job_aspiration = student.get_educational_info().get_job_aspiration()

    # predict the cluster number using the specified model (already trained)
    job_cluster = predict_job_cluster(student_job_aspiration, CAREER_MODEL_PATHS_DICT)
    logging.info(f'Predicted job cluster number is: {job_cluster}')

    # get the list of top k job titles based on job cluster number
    recommendations = get_top_k_job_titles(CAREER_BASE_DATA_PATH, job_cluster, k)

    df_recommendations = pd.DataFrame(recommendations, columns=['Job Title Recommendation'])

    return df_recommendations


def predict_job_cluster(job_aspiration_text, CAREER_MODEL_PATHS_DICT):
    # load the specified models from local
    model_classifier = joblib.load(CAREER_MODEL_PATHS_DICT['classifier'])
    model_embeddings = Doc2Vec.load(CAREER_MODEL_PATHS_DICT['text_embeddings'])

    # get d2v embeddings of the student's text
    text_embeddings = get_individual_d2v_embeddings(job_aspiration_text, model_embeddings)

    # feed the text embeddings to the model 
    predicted_cluster = model_classifier.predict([text_embeddings])[0]

    return predicted_cluster



def get_top_k_job_titles(CAREER_BASE_DATA_PATH, job_cluster, k):
    # read the local dataframe with labeled job clusters
    df_job_postings = pd.read_csv(CAREER_BASE_DATA_PATH, index_col=0)

    recommendations = df_job_postings.loc[df_job_postings['cluster']==job_cluster]['Title'].value_counts().index[:k]
    recommendations = recommendations.tolist()
    
    return recommendations