import shutil
import os
import os.path


class location:
    def loc1():
        geoposition = "C:/"
        name = "Secret Folder"
        path = os.path.join(geoposition, name)
        if os.path.isabs(path):
            shutil.rmtree(path)
            print("Complete")
            import Border
            os.startfile('Clear_Disk')
        else:
            raise ValueError("Location not identified {}".format(path))

    loc1()
