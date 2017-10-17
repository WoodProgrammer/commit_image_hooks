from builder import Builder
import requests,time
dev = Builder()
image_status = dev.build_image()


if  image_status[0]:
    try:
        r = requests.put('http://localhost:5000/{}'.format('project_1'), data={"status": "BUILT "})
        print "POSTED" + str(r.status_code)

    except:
        print "ERROR occured while PUT the data to the API "

    print "Image {} builded . hour: {}  date :  {} ".format(image_status[1].id, time.strftime("%H:%M:%S"),
                                                             time.strftime("%d/%m/%Y"))


elif image_status[0] == False:


    try:

        r = requests.put('http://localhost:5000/{}'.format('project_1'), data={"status": "NOT BUILD "})
        print "Image {}    Not Builded False .!  ".format(image_status[1].id)
    except:
        print "Image building attempt failed on last commit  {}".format('hebele')


