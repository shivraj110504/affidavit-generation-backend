def generate_affidavit_text(data):
    return f"""
ANNEXURE ‘I’

AFFIDAVIT

I, {data['name']}, son/daughter/wife of Shri {data['father_name']},
residing at {data['address']},
Date of Birth {data['dob']},
being an applicant for issue of passport, do hereby solemnly affirm and state the following:

1. That the names of my parents and spouse are as follows:
   (i) Father : {data['father_name']}
   (ii) Mother : {data['mother_name']}
   (iii) Wife/Husband : {data['spouse_name']}

2. That I am a continuous resident at the above mentioned address from {data['residence_from']}.

3. That I am a citizen of India and have not acquired the citizenship of another country.

4. That I have not been convicted by any court in India during the last five years.

5. That no criminal proceedings are pending against me.

6. That no warrant or summons has been issued against me.

7. That I will not engage in activities prejudicial to the sovereignty and integrity of India.

Place: {data['place']}
Date: {data['date']}

DEPONENT

VERIFICATION

Verified on {data['date']} at {data['place']} that the contents of the affidavit are true.

DEPONENT
"""
