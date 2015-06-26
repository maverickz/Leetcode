import json
import sys
import logging
import requests

token = None
logging.basicConfig(stream = sys.stderr)
logging.getLogger("client_ctrl.log").setLevel(logging.INFO)
log = logging.getLogger("client_ctrl.log")


def get_section_details(token):
    url_resource = "https://api.clever.com/v1.1/sections"
    headers = {'Authorization': token}
    
    r = requests.get(url_resource, headers=headers)
    if r.status_code != requests.codes.ok:
        log.error("Response: %s" % r.text)
        return None
    else:
        log.debug("%s" % json.dumps(json.loads(r.text), sort_keys=True, indent=4))
        sections = json.loads(r.text)
        return sections.get('data', None)

def get_avg_section_size(sections):
        total_students = 0
        num_sections = len(sections)
        for section in sections:
            total_students += len(section['data']['students'])
        avg_section_size = total_students / float(num_sections)
        return round(avg_section_size, 2)


if __name__ == '__main__':
    try:
        sections = get_section_details('Bearer DEMO_TOKEN')
        if sections:
            avg_section_size = get_avg_section_size(sections)
            log.info("Avg section size: %.2f" % avg_section_size)
    except:
        log.error("Unexpected error:", sys.exc_info()[0])
    
    

