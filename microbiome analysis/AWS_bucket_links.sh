#!/bin/bash

aws s3 ls s3://ai-for-life-sciences-2/ --no-sign-request --recursive | awk '{print "https://ai-for-life-sciences-2.s3.amazonaws.com/" $4}' > bucket-2-objects_url.txt


aws s3 ls s3://ai-for-life-sciences-1/ --no-sign-request --recursive | awk '{print "https://ai-for-life-sciences-2.s3.amazonaws.com/" $4}' > bucket-1-objects_url.txt