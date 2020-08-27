from flask import jsonify
from flask import Flask, request

import config

app = Flask(__name__)
		
@app.route('/servicecharge', methods=['GET'])
def debit():
	amount = request.args.get('amount')
	amt = int(amount)
	if amt:
	    if amt>0 and amt<=10000:
	        a= 0
	        a= str(a)
	        return a    
	    if amt>10000 and amt<=50000:
	        a= (amt*1.2)/100
	        a= str(a)
	        return a
	    if amt>50000 and amt<=100000:
	        a= (amt*1.8)/100
	        a= str(a)
	        return a
	    if amt>100000:
	        a= (amt*90)/100
	        a= str(a)
	        return a 
		
	else:
		return "Required field/fields is/are missing"
		
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
