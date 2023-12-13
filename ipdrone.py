#coded by N17RO (noob hackers)

#modules required
import argparse
import requests, json
import sys
from sys import argv
import os

#arguments and parser

parser = argparse.ArgumentParser()

parser.add_argument ("-v", help= "target/host IP address", type=str, dest='target', required=True )

args = parser.parse_args()

#colours used
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

#banner of script
print (red+"""

██╗██████╗ ██████╗ ██████╗  ██████╗ ███╗   ██╗███████╗
██║██╔══██╗██╔══██╗██╔══██╗██╔═══██╗████╗  ██║██╔════╝
██║██████╔╝██║  ██║██████╔╝██║   ██║██╔██╗ ██║█████╗  
██║██╔═══╝ ██║  ██║██╔══██╗██║   ██║██║╚██╗██║██╔══╝  
██║██║     ██████╔╝██║  ██║╚██████╔╝██║ ╚████║███████╗
╚═╝╚═╝     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                                                      v 1.0
"""+red)
print (lgreen+bold+"         <===[[ coded by N17RO ]]===> \n"+clear)
print (yellow+bold+"   <---(( search on youtube Noob Hackers ))--> \n"+clear)


ip = args.target

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = lgreen+bold+"[$]"
        b = cyan+bold+"[$]"
        print (a, "[Victim]:", data['query'])
        print(red+"<--------------->"+red)
        print (b, "[ISP]:", data['isp'])
        print(red+"<--------------->"+red)
        print (a, "[Organisation]:", data['org'])
        print(red+"<--------------->"+red)
        print (b, "[City]:", data['city'])
        print(red+"<--------------->"+red)
        print (a, "[Region]:", data['region'])
        print(red+"<--------------->"+red)
        print (b, "[Longitude]:", data['lon'])
        print(red+"<--------------->"+red)
        print (a, "[Latitude]:", data['lat'])
        print(red+"<--------------->"+red)
        print (b, "[Time zone]:", data['timezone'])
        print(red+"<--------------->"+red)
        print (a, "[Zip code]:", data['zip'])
        print (" "+yellow)

except KeyboardInterrupt:
        print ('Terminating, Bye'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[~]"+" check your internet connection!"+clear)
sys.exit(1)
Coinlover6923@gmail.com 
![Auto Assign](https://github.com/Andrapple-1-0/demo-repository/actions/workflows/auto-assign.yml/badge.svg)

![Proof HTML](https://github.com/Andrapple-1-0/demo-repository/actions/workflows/proof-html.yml/badge.svg)

# Welcome to your organization's demo respository
This code repository (or "repo") is designed to demonstrate the best GitHub has to offer with the least amount of noise.

The repo includes an `index.html` file (so it can render a web page), two GitHub Actions workflows, and a CSS stylesheet dependency.
SamsungBrowser/23.0 cheome/115.0.0.0 safari/537.36
Coinlover6923@gmail.com 
README.md
Coinlover6923@gmail.com 
I'm trying to put facebook app what's app bueisness and what's app together help plese
Andrapple-1-0 
Android_all_my_files for the people!!
*[ ] SamsungBrowser/23.0 cheome/115.0.0.0 safari/537.36http://mzl.la/1BsPDaX*
Coinlover6923@gmail.com
buymycoins3@gmail.com
tjmdonald@gmail.com
https://www.google.com/webhp?client=firefox-b-1-m&channel=tshttps://www.ecosia.org/search?q=%shttps://www.ecosia.org/search?q=%shttp://www.google.com/m?client=ms-android-charter-us-rvc3&source=android-homehttps://www.whatsmybrowser.org/b/URCO9slack://T0HSL38JD/magic-login/6318144925602-bdb2f61a5808fc2adc921a10e003e2d7aa631d51fb07f57cf929bedb7fbdc03b?id=1https://www.facebook.com/marketplace/item/672305121442686/?mibextid=dXMIcHhttps://call.whatsapp.com/video/XyXkfAKxF1ozII8FAmMvwYabanamichael74@gmail.comhttps://m.facebook.com/story.php?story_fbid=pfbid0ux4djTKY3gBhxyZqEiEws18g5HicDTpPuufCduSWZ7BejTfpGCi1LfYmkCNAWUbHl&id=100090238777069&mibextid=Nif5ozhttps://m.facebook.com/story.php?story_fbid=pfbid02kQoayWw7VoonmgNFnC9GxibGUt4CvajnN63fTVZ6UgCdrE3BA1A5kN2EzMyfXvx9l&id=100090238777069&mibextid=Nif5ozhttps://youtu.be/Dw9VmOLwxoMWORKOS_API_KEY='sk_example_123456789'
WORKOS_CLIENT_ID='client_123456789'
https://developer.microsoft.com/en-us/graph/graph-explorer?request=me%2Fdrive%2Froot%2Fchildren&method=GET&version=v1.0&GraphUrl=https://graph.microsoft.comhttps://developer.microsoft.com/en-us/graph/graph-explorer?request=me%2Fdrive%2Froot%2Fchildren&method=GET&version=v1.0&GraphUrl=https://graph.microsoft.comPOST https://login.microsoftonline.com/common/oauth2/v2.0/token
Content-Type: application/x-www-form-urlencoded
client_id={client_id}&redirect_uri={redirect_uri}&clie{
sdk: "8.0";
/**
Establishes the messaging parameters used to setup the post message communications between
picker and host application
/
messaging: {
/*
A unique id assigned by the host app to this File Picker instance.
/
channelId: string;
/*
The host app's authority, used as the target origin for post-messaging.
/
origin: string;
};
/*
Configuration for the entry location to which the File Picker will navigate on load.
The File Picker app will prioritize path-based navigation if provided, falling back to other address forms
on error (in case of Site redirection or content rename) or if path information is not provided.
/
entry: {
sharePoint?: {
/*
Specify an exact SharePoint content location by path segments.
/
byPath?: {
/*
Full URL to the root of a Web, or server-relative URL.
@example
'https://contoso-my.sharepoint.com/personal/user_contoso_com'
@example
'/path/to/web'
@example
'subweb'
/
web?: string;
/*
Full URL or path segement to identity a List.
If not preceded with a  /  or a URL scheme, this is assumed to be a list in the specified web.
@example
'Shared Documents'
@example
'/path/to/web/Shared Documents'
@example
'https://contoso.sharepoint.com/path/to/web/Shared Documents'
/
list?: string;
/*
Path segment to a folder within a list, or a server-relative URL to a folder.
@example
'General'
@example
'foo/bar'
@example
'/path/to/web/Shared Documents/General'
/
folder?: string;
};
};
/*
Indicates that the File Picker should start in the user's OneDrive.
/
oneDrive?: {
/*
Indicates that File Picker should start in the user's recent files.
/
recent?: {};
/*
Specifies that File Picker should start in the user's Files tab.
/
files?: {
/*
Path segment for sub-folder within the user's OneDrive.
@example
'Pictures'
@example
'/personal/user_contoso_com/Documents/Attachments'
/
folder?: string;
}
};
};
/*
Specifies how to enable a Search behavior.
/
search?: {
enabled: boolean;
},
/*
Providing this object indicates that the host app can provide OAuth tokens
via the existing messaging support.
/
authentication: {};
/*
Specifies what types of items may be picked and where they come from. Support for these features is inconsistent currently for external applications.
/
typesAndSources?: {
/*
Specifies the general category of items picked. Switches between 'file' vs. 'folder' picker mode,
or a general-purpose picker.
@default 'all'
/
mode?: "files" | "folders" | "all";
/*
Set of file extensions or 'item types'.
File extensions should be lower-case and prefixed with a  . .
Item types should be lowercase and come from the following set:
photo
video
audio
folder
file
@default  ['folder']  if  itemTypes  is 'folders', otherwise  [] 
/
filters?: string[];
/*
Configures whether or not specific pivots may be browsed for content by the user.
/
pivots?: {
recent?: boolean;
oneDrive?: boolean;
sharedLibraries?: boolean;
};
};
/*
Specified how many items may be picked.
/
selection?: {
/*
@default 'single'
/
mode?: "single" | "multiple" | "pick";
};
/*
Specifies what happens when users pick files and what the user may do with files in the picker.
/
commands?: {
/*
Sets the default 'pick' behavior once the user selects items.
/
pick?: {
/*
A custom label to apply to the button to pick the items.
The default varies based on  action , but is typically 'Select'.
This string must be localized if provided.
/
label?: string;
};
close?: {
/*
A custom label to apply to the button to close the picker.
The default is 'Cancel'.
This string must be localized if provided.
/
label?: string;
};
};
/*
Specifies accessibility cues such as auto-focus behaviors.
/
accessibility?: {
/*
The File Picker can provide a 'tab-loop' behavior within its frame or window.
/
enableFocusTrap?: boolean;
/*
The File Picker can automatically grab focus once it loads.
/
trapFocusOnLoad?: boolean;
/*
By default, the File Picker does not initialally highlight the focused elements,
but does so once a user starts using the keyboard. Set this option to force
an initial highlight.
/
showFocusOnLoad?: boolean;
};
tray?: {
/*
Configures a component to render in the picker tray to the left of the commands.
@default 'selection-summary'
/
prompt?: "selection-summary" | "save-as";
/*
Configures use of the 'save-as' prompt.
/
saveAs?: {
/*
Default file name to show in 'save-as' prompt.
*/
fileName?: [string;
](SamsungBrowser/23.0 cheome/115.0.0.0http://mzl.la/1BsPDaX)      };
};
}https://developer.microsoft.com/en-us/graph/graph-explorer?request=me%2Fdrive%2Froot%2Fchildren&method=GET&version=v1.0&GraphUrl=https://graph.microsoft.comhttps://myapp.com/auth-redirect#access_token=EwC...EB
&authentication_token=eyJ...3EM&token_type=bearer&expires_in=3600
&scope=onedrive.readwrite&user_id=3626...1dwinget install "Visual Studio Community 2022"  --override "--add Microsoft.VisualStudio.Workload.NativeDesktop  Microsoft.VisualStudio.ComponentGroup.WindowsAppSDK.Cpp"  -s msstore
