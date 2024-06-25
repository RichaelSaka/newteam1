import csv

# takes in user's intended role and industry as well as job industry and industry role
def job_filter(user_industry, user_role, industry_role, job_industries):
    # Check if the user's job and industry matches that of the job posted
    if (user_industry in job_industries) and (user_role == industry_role):
        return True
    else: 
        return False


def get_predicate(user_inds, user_role):
    def predicate(job):
        job_ind = job["indusry"]
        job_role = job["position"]
        return job_role.lower() == user_role.lower() and job_ind.lower() in user_inds.lower()
    return predicate
