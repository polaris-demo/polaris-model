import urllib.request

with urllib.request.urlopen('https://polaris-sample-workflow-data.s3.us-west-1.amazonaws.com/data.pkl') as f:
    with open('/mnt/vol/repo/artifacts/data.pkl', 'wb') as o:
        o.write(f.read())
