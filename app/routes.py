from flask import redirect, request, render_template
from . import application
import json
import os

@application.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@application.route('/noop', methods=['GET', 'POST'])
def amf_module():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        content = None
        with open(f.filename, 'r') as ff:
            content = json.load(ff)

        ####################################
        #
        #   call the code for the specific 
        #   AMF module here....
        #
        #####################################

        result_xaif = content  ## "content" needs to be replaced by the resulting xaif data 
        if os.path.exists(f.filename):
            os.remove(f.filename)
        return result_xaif
    elif request.method == 'GET':
        return render_template('index.html')
        
 
 
