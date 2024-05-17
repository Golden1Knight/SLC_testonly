import montrevix.slc.extensions.detector as detc
global commandCustomList
commandCustomList = ["a", "b"]

def loadInterpreter(file="montrevix/slc/apps/langinterpreter.lngi"):
    global commandCustomList
    settingsSLC = {
        'file': file,
        'prefix': 'a'
    }
    detc.detector(settingsSLC, 'AllForAll')