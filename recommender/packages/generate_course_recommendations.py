'''
This is the layer where we generate course-related recommendations, 
which would later be weighted and aggregated to generate final recommendations for a particualr student.

The course-related recommendation types include:
- course_basic_info TODO
- course_content: course description and learning outcomes
- course_assessment TODO
'''

import logging

from ontology_profiles.student_profile.Student import *
from ontology_profiles.student_profile.PersonalInfo import *
from ontology_profiles.student_profile.EducationalInfo import *

from ontology_profiles.course_profile.Course import *
from ontology_profiles.course_profile.CourseBasicInfo import *
from ontology_profiles.course_profile.CourseContent import *

from helper_functions import *
from generate_course_similarity import *
from configs import *
from apis import course_database_api, subject_domain_database_api

# logging.getLogger().setLevel(logging.DEBUG)

'''
FUNCTION
- Generate top k COURSE recommendations for the particular student
- Separate FIXME
Return: DATAFRAME consisting of top k recommendations (Course Code)
'''
def generate_course_recommendations(student: Student, COURSE_REC_TYPES: list, COURSE_BASE_DATA_PATH, COURSE_ADDITIONAL_DATA_PATH_DICT, similarity_type='cosine', k=5):
    # 1. convert course dataset into a list of Course instances
    courses = course_database_api.convert_to_courses(COURSE_BASE_DATA_PATH, COURSE_ADDITIONAL_DATA_PATH_DICT)

    # 2. generate all similarity scores by comparing the student provided info and all courses in our database
    # FIXME: need to change this to incorporate the LIST of course rec types instead of only one type
    df_course_content_similarities = generate_all_course_similarities(student, courses, COURSE_MODEL_PATHS_DICT[COURSE_REC_TYPES[0]], similarity_type, COURSE_REC_TYPES[0])

    # 3. return the top k most similar courses as final recommendations
    df_recommendations = df_course_content_similarities.head(k)
    #[['Course Code', 'Course Title']]

    return df_recommendations