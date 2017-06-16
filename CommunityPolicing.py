import subprocess
# Need to check if the following is started:

def start_neo4j():
    command = 'bash neo4j-community-3.2.0/bin/neo4j status'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    if output == "b'Neo4j is not running\n'":
        print(starting)
        try:
            command = 'bash neo4j-community-3.2.0/bin/neo4j start'
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            output, error = process.communicate()
            print(output, error)
            return(True)
        except Exception as e:
            return(e)
    else:
        print("already running")
        

# neo4j in /neo4j-community-3.2.0
# Web2Py server in /web2py
# proxy server?

start_neo4j()
