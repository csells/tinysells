import webapp2

redirects = [
  {
    "Code": 1,
    "Link": "http://www.sellsbrothers.com/",
    "IsActive": False
  },
  {
    "Code": 2,
    "Link": "http://www.microsoft.com",
    "IsActive": False
  },
  {
    "Code": 3,
    "Link": "http://www.codeproject.com",
    "IsActive": False
  },
  {
    "Code": 4,
    "Link": "http://windowsforms.net/articles/notifyiconapplications.aspx",
    "IsActive": True
  },
  {
    "Code": 5,
    "Link": "http://msdn.microsoft.com/msdntv/episode.aspx?xml=episodes/en/20040401WinFormsMH/manifest.xml",
    "IsActive": True
  },
  {
    "Code": 6,
    "Link": "http://www.windowsforms.net/Samples/download.aspx?PageId=1&ItemId=174&tabindex=4",
    "IsActive": True
  },
  {
    "Code": 7,
    "Link": "http://www.pinvoke.net/",
    "IsActive": True
  },
  {
    "Code": 8,
    "Link": "http://www.genghisgroup.com/",
    "IsActive": True
  },
  {
    "Code": 9,
    "Link": "http://blogs.msdn.com/mharsh/archive/2005/03/14/395304.aspx",
    "IsActive": True
  },
  {
    "Code": 10,
    "Link": "http://www.wd-mag.com/documents/s=7547/win0212d/",
    "IsActive": True
  },
  {
    "Code": 11,
    "Link": "http://msdn.microsoft.com/library/default.asp?url=/library/en-us/htmlhelp/html/hwMicrosoftHTMLHelpDownloads.asp",
    "IsActive": True
  },
  {
    "Code": 12,
    "Link": "http://blogs.msdn.com/jfoscoding/archive/2005/03/04/385625.aspx",
    "IsActive": True
  },
  {
    "Code": 13,
    "Link": "http://www.mikedub.net/",
    "IsActive": True
  },
  {
    "Code": 14,
    "Link": "http://www.microsoft.com/windowsxp/using/accessibility/highcontrast.mspx",
    "IsActive": True
  },
  {
    "Code": 15,
    "Link": "http://msdn.microsoft.com/msdnmag/issues/04/02/TimersinNET/default.aspx",
    "IsActive": True
  },
  {
    "Code": 16,
    "Link": "http://msdn2.microsoft.com/en-us/library/0s71x931(vs.71).aspx",
    "IsActive": True
  },
  {
    "Code": 17,
    "Link": "http://www.microsoft.com/globaldev/DrIntl/faqs/Complex.mspx#E6",
    "IsActive": True
  },
  {
    "Code": 18,
    "Link": "http://si.wikipedia.org/wiki/Wikipedia:Sinhala_font",
    "IsActive": True
  },
  {
    "Code": 19,
    "Link": "http://www.windowsforms.com/Samples/Go%20To%20Market/Tool%20Strips/ToolStrip%20GTM.doc#Toc116357041",
    "IsActive": True
  },
  {
    "Code": 20,
    "Link": "http://msdn2.microsoft.com/en-us/library/system.windows.forms.visualstyles.visualstylerenderer.aspx",
    "IsActive": True
  },
  {
    "Code": 21,
    "Link": "http://msdn2.microsoft.com/en-us/library/system.componentmodel.design.designertransaction.aspx",
    "IsActive": True
  },
  {
    "Code": 22,
    "Link": "http://www.windowsforms.net/Default.aspx?tabindex=4&tabid=49#Windows%20Forms%20V2%20Demo%20App",
    "IsActive": True
  },
  {
    "Code": 23,
    "Link": "http://www.codeguru.com/cpp_mfc/rsrc-simple.html",
    "IsActive": True
  },
  {
    "Code": 24,
    "Link": "http://msdn2.microsoft.com/en-us/library/1021kkz0(vs.71).aspx",
    "IsActive": True
  },
  {
    "Code": 25,
    "Link": "http://en.wikipedia.org/wiki/ISO_639",
    "IsActive": True
  },
  {
    "Code": 26,
    "Link": "http://en.wikipedia.org/wiki/ISO_3166",
    "IsActive": True
  },
  {
    "Code": 27,
    "Link": "http://www.microsoft.com/middleeast/msdn/visualstudio2005.aspx",
    "IsActive": True
  },
  {
    "Code": 28,
    "Link": "http://msdn2.microsoft.com/en-us/library/8eyb2ct1.aspx",
    "IsActive": True
  },
  {
    "Code": 29,
    "Link": "http://www.sellsbrothers.com/news/showTopic.aspx?ixTopic=1537",
    "IsActive": True
  },
  {
    "Code": 30,
    "Link": "http://www.verisign.com/",
    "IsActive": True
  },
  {
    "Code": 31,
    "Link": "http://www.interact-sw.co.uk/iangblog/2004/06/10/codeviewinvs",
    "IsActive": True
  },
  {
    "Code": 32,
    "Link": "http://www.aisto.com/roeder/dotnet/",
    "IsActive": True
  },
  {
    "Code": 33,
    "Link": "http://msdn2.microsoft.com/library/ahdd1h97(en-us,vs.80).aspx",
    "IsActive": True
  },
  {
    "Code": 34,
    "Link": "http://msdn2.microsoft.com/en-us/library/ahdd1h97(en-us,vs.80).aspx",
    "IsActive": True
  },
  {
    "Code": 35,
    "Link": "http://msdn.microsoft.com/library/default.asp?url=/library/en-us/dnwinforms/html/dragdrop_datagrid.asp",
    "IsActive": False
  },
  {
    "Code": 36,
    "Link": "http://msdn2.microsoft.com/en-us/library/ms996423.aspx",
    "IsActive": True
  },
  {
    "Code": 37,
    "Link": "http://www.w3.org/TR/wsdl",
    "IsActive": True
  },
  {
    "Code": 38,
    "Link": "http://www.adaptivepath.com/publications/essays/archives/000385.php",
    "IsActive": True
  },
  {
    "Code": 39,
    "Link": "http://msdn.microsoft.com/msdnmag/issues/02/04/net/",
    "IsActive": True
  },
  {
    "Code": 40,
    "Link": "http://www.pinvoke.net/default.aspx/shell32/SHAddToRecentDocs.html",
    "IsActive": True
  },
  {
    "Code": 41,
    "Link": "http://www.codeproject.com/vb/net/vbnetdragdrop.asp",
    "IsActive": True
  },
  {
    "Code": 42,
    "Link": "http://msdn2.microsoft.com/en-us/library/system.windows.forms.control(vs.71).aspx",
    "IsActive": True
  },
  {
    "Code": 43,
    "Link": "http://blogs.msdn.com/cbrumme/archive/2003/05/06/51385.aspx",
    "IsActive": True
  },
  {
    "Code": 44,
    "Link": "http://msdn.microsoft.com/msdnmag/issues/04/10/Bootstrapper/",
    "IsActive": True
  },
  {
    "Code": 45,
    "Link": "http://msdn.microsoft.com/smartclient/",
    "IsActive": True
  },
  {
    "Code": 46,
    "Link": "http://www.microsoft.com/technet/archive/security/topics/secaps/authcode.mspx",
    "IsActive": True
  },
  {
    "Code": 47,
    "Link": "http://www.rsasecurity.com/rsalabs/node.asp?id=2308",
    "IsActive": True
  },
  {
    "Code": 48,
    "Link": "http://msdn2.microsoft.com/en-us/library/ms996418.aspx",
    "IsActive": True
  },
  {
    "Code": 49,
    "Link": "http://www.microsoft.com/globaldev/handson/dev/mslu_announce.mspx",
    "IsActive": True
  },
  {
    "Code": 50,
    "Link": "http://msdn2.microsoft.com/en-us/library/ms809982.aspx",
    "IsActive": True
  },
  {
    "Code": 51,
    "Link": "http://www.sellsbrothers.com/links/dbox/enumgen.zip",
    "IsActive": True
  },
  {
    "Code": 52,
    "Link": "http://msdn2.microsoft.com/en-us/library/fxet95e8(vs.71).aspx",
    "IsActive": True
  },
  {
    "Code": 53,
    "Link": "http://www.west-wind.com/presentations/iis5Debug.htm",
    "IsActive": True
  },
  {
    "Code": 54,
    "Link": "http://www.w3.org/TR/soap12-part1/",
    "IsActive": True
  },
  {
    "Code": 55,
    "Link": "http://msdn2.microsoft.com/en-us/library/ms995710.aspx",
    "IsActive": True
  },
  {
    "Code": 56,
    "Link": "http://www.joelonsoftware.com/articles/buildingcommunitieswithso.html",
    "IsActive": True
  },
  {
    "Code": 57,
    "Link": "http://www.owasp.org/documentation/topten.html",
    "IsActive": True
  },
  {
    "Code": 58,
    "Link": "http://msdn2.microsoft.com/en-us/library/f520z3b3(VS.80).aspx",
    "IsActive": True
  },
  {
    "Code": 59,
    "Link": "http://lab.msdn.microsoft.com/productfeedback/viewfeedback.aspx?feedbackid=a09357fe-32fa-43a1-9223-95bc2c38765e",
    "IsActive": True
  },
  {
    "Code": 60,
    "Link": "http://msdn2.microsoft.com/en-us/library/ms974281.aspx",
    "IsActive": True
  },
  {
    "Code": 61,
    "Link": "http://www.microsoft.com/msj/1299/containment/containment.aspx",
    "IsActive": True
  },
  {
    "Code": 62,
    "Link": "http://msdn.microsoft.com/library/default.asp?url=/library/en-us/sdkintro/sdkintro/devdoc_platform_software_development_kit_start_page.asp",
    "IsActive": True
  },
  {
    "Code": 63,
    "Link": "http://www.microsoft.com/downloads/details.aspx?familyid=c16ae515-c8f4-47ef-a1e4-a8dcbacff8e3",
    "IsActive": True
  },
  {
    "Code": 64,
    "Link": "http://blogs.msdn.com/bencon/archive/2006/01.aspx",
    "IsActive": True
  },
  {
    "Code": 65,
    "Link": "http://msdn2.microsoft.com/en-us/library/ms752300.aspx#Path_Syntax",
    "IsActive": True
  },
  {
    "Code": 66,
    "Link": "http://msdn2.microsoft.com/en-us/library/system.windows.data.relativesourcemode.aspx",
    "IsActive": True
  },
  {
    "Code": 67,
    "Link": "http://msdn2.microsoft.com/en-gb/library/aa970069.aspx",
    "IsActive": True
  },
  {
    "Code": 68,
    "Link": "http://msdn2.microsoft.com/en-us/library/default.aspx",
    "IsActive": True
  },
  {
    "Code": 69,
    "Link": "http://mathworld.wolfram.com/BezierCurve.html",
    "IsActive": True
  },
  {
    "Code": 70,
    "Link": "http://en.wikipedia.org/wiki/B%C3%A9zier_curve",
    "IsActive": True
  },
  {
    "Code": 71,
    "Link": "http://www.microsoft.com/whdc/xps/viewxps.mspx",
    "IsActive": True
  },
  {
    "Code": 72,
    "Link": "http://www.microsoft.com/whdc/xps/default.mspx",
    "IsActive": True
  },
  {
    "Code": 73,
    "Link": "http://adoguy.com/wpfesamples/slideshow.aspx",
    "IsActive": True
  },
  {
    "Code": 74,
    "Link": "http://msdn2.microsoft.com/en-us/system.windows.documents.typography.aspx",
    "IsActive": True
  },
  {
    "Code": 75,
    "Link": "http://www.codeplex.com/3DTools/Release/ProjectReleases.aspx?ReleaseId=577",
    "IsActive": True
  },
  {
    "Code": 76,
    "Link": "http://www.codeplex.com/3DTools",
    "IsActive": True
  },
  {
    "Code": 77,
    "Link": "http://www.sjbrown.co.uk/?article=quaternions",
    "IsActive": True
  },
  {
    "Code": 78,
    "Link": "http://blogs.msdn.com/mikehillberg/archive/2006/09/14/WpfTraceSources.aspx",
    "IsActive": True
  },
  {
    "Code": 79,
    "Link": "http://msdn2.microsoft.com/en-us/library/system.diagnostics.presentationtracesources.aspx",
    "IsActive": True
  },
  {
    "Code": 80,
    "Link": "http://msdn2.microsoft.com/library/3e8s7xdd.aspx",
    "IsActive": True
  },
  {
    "Code": 81,
    "Link": "http://chortle.ccsu.edu/VectorLessons/index.html",
    "IsActive": True
  },
  {
    "Code": 82,
    "Link": "http://blogs.msdn.com/mharsh/archive/2007/03/26/lumines-live-60-second-top-score-in-wpf-e.aspx",
    "IsActive": True
  },
  {
    "Code": 83,
    "Link": "http://www.screenedit.co.uk/sevideo/9992/9992.htm",
    "IsActive": True
  },
  {
    "Code": 84,
    "Link": "http://blogs.msdn.com/delay/archive/2007/05/01/the-web-just-got-even-better-silverlight-announced-at-mix07.aspx",
    "IsActive": True
  },
  {
    "Code": 85,
    "Link": "http://msdn2.microsoft.com/en-us/library/ms771662.aspx",
    "IsActive": True
  },
  {
    "Code": 86,
    "Link": "http://www.sellsbrothers.com/writing/default.aspx?content=dotnet2customsettingsprovider.htm",
    "IsActive": True
  },
  {
    "Code": 87,
    "Link": "http://msdn.microsoft.com/msdnmag/issues/03/03/WindowsForms/default.aspx",
    "IsActive": True
  },
  {
    "Code": 88,
    "Link": "http://blogs.msdn.com/mswanson/articles/WPFToolsAndControls.aspx",
    "IsActive": True
  },
  {
    "Code": 89,
    "Link": "http://blogs.msdn.com/wpfsdk/archive/2006/10/26/Uncommon-Dialogs--Font-Chooser-and-Color-Picker-Dialogs.aspx",
    "IsActive": True
  },
  {
    "Code": 90,
    "Link": "http://msdn2.microsoft.com/en-gb/library/ms771765.aspx",
    "IsActive": True
  },
  {
    "Code": 91,
    "Link": "http://msdn2.microsoft.com/en-us/library/system.componentmodel.asyncoperationmanager.aspx",
    "IsActive": True
  },
  {
    "Code": 92,
    "Link": "http://msdn2.microsoft.com/en-gb/library/ms750478.aspx#NavigationService",
    "IsActive": True
  },
  {
    "Code": 93,
    "Link": "http://msdn2.microsoft.com/en-us/library/ms742522.aspx",
    "IsActive": True
  },
  {
    "Code": 94,
    "Link": "http://www.ondotnet.com/pub/a/dotnet/2003/01/20/winformshosting.html",
    "IsActive": True
  },
  {
    "Code": 95,
    "Link": "http://msdn2.microsoft.com/en-us/library/ms756482.aspx",
    "IsActive": True
  },
  {
    "Code": 96,
    "Link": "http://www.ietf.org/rfc/rfc2396.txt",
    "IsActive": True
  },
  {
    "Code": 97,
    "Link": "http://msdn.microsoft.com/msdnmag/issues/06/00/PureC/default.aspx",
    "IsActive": True
  },
  {
    "Code": 98,
    "Link": "http://blogs.msdn.com/seema/archive/2006/10/25/layered-windows-sw-is-sometimes-faster-than-hw.aspx",
    "IsActive": True
  },
  {
    "Code": 99,
    "Link": "http://www.unicode.org/reports/tr9/",
    "IsActive": True
  },
  {
    "Code": 100,
    "Link": "http://www.interact-sw.co.uk/iangblog/2007/03/28/wpfmagnifyupdate",
    "IsActive": True
  },
  {
    "Code": 101,
    "Link": "http://www.microsoft.com/whdc/xps/viewxps.mspx",
    "IsActive": True
  },
  {
    "Code": 102,
    "Link": "http://msdn2.microsoft.com/en-us/library/ms753388.aspx",
    "IsActive": True
  },
  {
    "Code": 103,
    "Link": "http://msdn2.microsoft.com/en-gb/library/aa972163.aspx",
    "IsActive": True
  },
  {
    "Code": 104,
    "Link": "http://www.sellsbrothers.com/news/showTopic.aspx?ixTopic=2053",
    "IsActive": True
  },
  {
    "Code": 105,
    "Link": "http://msdn.microsoft.com/vstudio/express/downloads/",
    "IsActive": True
  },
  {
    "Code": 106,
    "Link": "http://msdn2.microsoft.com/library/ms746621.aspx",
    "IsActive": True
  },
  {
    "Code": 107,
    "Link": "http://msdn2.microsoft.com/library/1021kkz0.aspx",
    "IsActive": True
  },
  {
    "Code": 108,
    "Link": "http://msdn2.microsoft.com/en-us/library/ms735322.aspx",
    "IsActive": True
  },
  {
    "Code": 109,
    "Link": "http://fortes.com/2007/03/20/bindablerun/",
    "IsActive": True
  },
  {
    "Code": 110,
    "Link": "http://www.ecma-international.org/memento/TC45.htm",
    "IsActive": True
  },
  {
    "Code": 111,
    "Link": "http://msdn2.microsoft.com/en-us/library/ms737408.aspx",
    "IsActive": True
  },
  {
    "Code": 112,
    "Link": "http://wpf.netfx3.com/files/folders/controls/entry8196.aspx",
    "IsActive": True
  },
  {
    "Code": 113,
    "Link": "http://msdn2.microsoft.com/library/aa970564.aspx",
    "IsActive": True
  },
  {
    "Code": 114,
    "Link": "http://blogs.msdn.com/tims/search.aspx?q=%22great+wpf+applications%22",
    "IsActive": True
  },
  {
    "Code": 115,
    "Link": "http://blogs.msdn.com/tims/articles/475132.aspx",
    "IsActive": True
  },
  {
    "Code": 116,
    "Link": "http://blogs.msdn.com/karstenj/archive/2006/06/15/632639.aspx",
    "IsActive": True
  },
  {
    "Code": 117,
    "Link": "http://msdn2.microsoft.com/en-us/netframework/aa663326.aspx",
    "IsActive": True
  },
  {
    "Code": 118,
    "Link": "http://www.codeproject.com/WPF/",
    "IsActive": True
  },
  {
    "Code": 119,
    "Link": "http://www.thirteen23.com/labs.html",
    "IsActive": True
  },
  {
    "Code": 120,
    "Link": "http://contentpresenter.com",
    "IsActive": True
  },
  {
    "Code": 123,
    "Link": "http://visualstudiogallery.msdn.microsoft.com/en-us/df3541c3-d833-4b65-b942-989e7ec74c87",
    "IsActive": True
  },
  {
    "Code": 125,
    "Link": "http://msdn.microsoft.com/en-us/library/bb387122(VS.90).aspx",
    "IsActive": True
  },
  {
    "Code": 126,
    "Link": "http://sellsbrothers.com/Posts/Details/12699",
    "IsActive": True
  },
  {
    "Code": 127,
    "Link": "http://msdn.microsoft.com/en-us/data/ff707264.aspx",
    "IsActive": True
  },
  {
    "Code": 128,
    "Link": "http://sellsbrothers.com/Posts/Details/12700",
    "IsActive": True
  },
  {
    "Code": 129,
    "Link": "http://msdn.microsoft.com/en-us/ff714955.aspx",
    "IsActive": True
  },
  {
    "Code": 130,
    "Link": "http://microsoft.com/downloads/en/details.aspx?FamilyID=af18e652-9ea7-478b-8b41-8424b94e3f58",
    "IsActive": True
  },
  {
    "Code": 131,
    "Link": "http://msdn.microsoft.com/en-us/library/bb126445.aspx",
    "IsActive": True
  },
  {
    "Code": 132,
    "Link": "http://sellsbrothers.com/Posts/Details/12698",
    "IsActive": True
  },
  {
    "Code": 133,
    "Link": "http://hanselman.com/blog/SimpleCodeFirstWithEntityFramework4MagicUnicornFeatureCTP4.aspx",
    "IsActive": True
  },
  {
    "Code": 134,
    "Link": "http://msdn.microsoft.com/en-us/library/bb738685.aspx",
    "IsActive": True
  },
  {
    "Code": 135,
    "Link": "http://en.wiktionary.org/wiki/niladic",
    "IsActive": True
  },
  {
    "Code": 136,
    "Link": "http://blogs.msdn.com/b/adonet/archive/2008/03/26/stored-procedure-mapping.aspx",
    "IsActive": True
  },
  {
    "Code": 137,
    "Link": "http://sellsbrothers.com/posts/Details/12614",
    "IsActive": True
  },
  {
    "Code": 138,
    "Link": "http://odata.org/docs/[MC-APDSU].htm",
    "IsActive": True
  },
  {
    "Code": 139,
    "Link": "http://odata.org/developers/protocols/overview.aspx",
    "IsActive": True
  },
  {
    "Code": 140,
    "Link": "http://tools.ietf.org/html/rfc5023",
    "IsActive": True
  },
  {
    "Code": 141,
    "Link": "http://odata.org/developers/protocols/overview",
    "IsActive": True
  },
  {
    "Code": 142,
    "Link": "http://odata.org/media/6652/[mc-csdl][1].htm",
    "IsActive": True
  },
  {
    "Code": 143,
    "Link": "http://msdn.microsoft.com/en-us/library/ff478141.aspx",
    "IsActive": True
  },
  {
    "Code": 144,
    "Link": "http://msdn.microsoft.com/en-us/library/ee373841.aspx",
    "IsActive": True
  },
  {
    "Code": 145,
    "Link": "http://blogs.msdn.com/b/alexj/archive/2010/01/07/data-service-providers-getting-started.aspx",
    "IsActive": True
  },
  {
    "Code": 146,
    "Link": "http://www.odata.org/developers/articles",
    "IsActive": True
  },
  {
    "Code": 147,
    "Link": "http://blogs.msdn.com/b/astoriateam/archive/2010/02/02/server-paging-in-data-services.aspx",
    "IsActive": True
  },
  {
    "Code": 148,
    "Link": "http://en.wikipedia.org/wiki/List_of_HTTP_status_codes",
    "IsActive": True
  },
  {
    "Code": 149,
    "Link": "http://blogs.msdn.com/b/astoriateam/archive/tags/authentication",
    "IsActive": True
  },
  {
    "Code": 150,
    "Link": "http://en.wikipedia.org/wiki/Base64",
    "IsActive": True
  },
  {
    "Code": 151,
    "Link": "http://blogs.msdn.com/b/astoriateam/archive/2010/07/21/odata-and-authentication-part-7-forms-authentication.aspx",
    "IsActive": True
  },
  {
    "Code": 152,
    "Link": "http://sellsbrothers.com/Posts/Details/12697",
    "IsActive": True
  },
  {
    "Code": 153,
    "Link": "http://whatwg.org/specs/web-apps/current-work/multipage",
    "IsActive": True
  },
  {
    "Code": 154,
    "Link": "http://en.wikipedia.org/wiki/Cross-site_scripting",
    "IsActive": True
  },
  {
    "Code": 155,
    "Link": "http://code.msdn.microsoft.com/DataServicesJSONP",
    "IsActive": True
  },
  {
    "Code": 156,
    "Link": "http://www.ericdelabar.com/2008/05/metaprogramming-javascript.html",
    "IsActive": True
  },
  {
    "Code": 157,
    "Link": "http://sellsbrothers.com/Posts/Details/12716",
    "IsActive": True
  },
  {
    "Code": 158,
    "Link": "http://technet.microsoft.com/en-us/library/hh856045.aspx",
    "IsActive": True
  },
  {
    "Code": 159,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/br211786.aspx",
    "IsActive": True
  },
  {
    "Code": 160,
    "Link": "http://channel9.msdn.com/Events/BUILD/BUILD2011/BPS-1004",
    "IsActive": True
  },
  {
    "Code": 161,
    "Link": "http://channel9.msdn.com/Events/BUILD/BUILD2011/APP-395T",
    "IsActive": True
  },
  {
    "Code": 162,
    "Link": "http://msdn.microsoft.com/library/windows/apps/hh779072/",
    "IsActive": True
  },
  {
    "Code": 163,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh465424",
    "IsActive": True
  },
  {
    "Code": 164,
    "Link": "http://msdn.microsoft.com/library/windows/apps/br211474.aspx",
    "IsActive": True
  },
  {
    "Code": 165,
    "Link": "http://code.msdn.microsoft.com/windowsapps/ListView-custom-data-4dcfb128",
    "IsActive": True
  },
  {
    "Code": 166,
    "Link": "https://downloads.flipboard.com/android-beta/0a319c667/Flipboard-1.8.4-63-beta-release.apk",
    "IsActive": True
  },
  {
    "Code": 167,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh872191.aspx",
    "IsActive": True
  },
  {
    "Code": 168,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh780612.aspx",
    "IsActive": True
  },
  {
    "Code": 169,
    "Link": "http://w3.org/TR/css3-mediaqueries/",
    "IsActive": True
  },
  {
    "Code": 170,
    "Link": "http://msdn.microsoft.com/en-us/magazine/hh882445.aspx",
    "IsActive": True
  },
  {
    "Code": 171,
    "Link": "http://w3.org/TR/css3-grid-layout",
    "IsActive": True
  },
  {
    "Code": 172,
    "Link": "http://www.w3.org/TR/css3-grid-layout/#fraction-values-fr0",
    "IsActive": True
  },
  {
    "Code": 173,
    "Link": "http://www.lullabot.com/articles/responsive-adaptive-web-design ",
    "IsActive": True
  },
  {
    "Code": 174,
    "Link": "http://w3c.org/TR/css3-flexbox ",
    "IsActive": True
  },
  {
    "Code": 175,
    "Link": "http://w3.org/TR/css3-multicol",
    "IsActive": True
  },
  {
    "Code": 176,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh700394",
    "IsActive": True
  },
  {
    "Code": 177,
    "Link": "http://google.com/webfonts",
    "IsActive": True
  },
  {
    "Code": 178,
    "Link": "http://www.microsoft.com/typography/otspec/featurelist.htm",
    "IsActive": True
  },
  {
    "Code": 179,
    "Link": "http://css-tricks.com/css-content/",
    "IsActive": True
  },
  {
    "Code": 180,
    "Link": "http://pictos.cc",
    "IsActive": True
  },
  {
    "Code": 181,
    "Link": "http://www.entypo.com/",
    "IsActive": True
  },
  {
    "Code": 182,
    "Link": "http://somerandomdude.com/work/iconic/",
    "IsActive": True
  },
  {
    "Code": 183,
    "Link": "http://www.heydonworks.com/article/a-free-icon-web-font",
    "IsActive": True
  },
  {
    "Code": 184,
    "Link": "http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL",
    "IsActive": True
  },
  {
    "Code": 185,
    "Link": "http://heydonworks.com",
    "IsActive": True
  },
  {
    "Code": 186,
    "Link": "http://www.fontsquirrel.com/fontface/generator",
    "IsActive": True
  },
  {
    "Code": 187,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh767390.aspx",
    "IsActive": True
  },
  {
    "Code": 188,
    "Link": "http://www.bigbuckbunny.org",
    "IsActive": True
  },
  {
    "Code": 189,
    "Link": "http://www.w3.org/wiki/HTML/Elements/video",
    "IsActive": True
  },
  {
    "Code": 190,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh767373.aspx",
    "IsActive": True
  },
  {
    "Code": 191,
    "Link": "http://www.w3.org/TR/ttaf1-dfxp/",
    "IsActive": True
  },
  {
    "Code": 192,
    "Link": "http://dev.w3.org/html5/webvtt/",
    "IsActive": True
  },
  {
    "Code": 193,
    "Link": "http://yaml.org/ ",
    "IsActive": True
  },
  {
    "Code": 194,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh465962.aspx",
    "IsActive": True
  },
  {
    "Code": 195,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh452730.aspx",
    "IsActive": True
  },
  {
    "Code": 196,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh452791.aspx",
    "IsActive": True
  },
  {
    "Code": 197,
    "Link": "http://dlna.org",
    "IsActive": True
  },
  {
    "Code": 198,
    "Link": "http://go.microsoft.com/fwlink/p/?LinkId=215946",
    "IsActive": True
  },
  {
    "Code": 199,
    "Link": "http://www.khronos.org/webgl/ ",
    "IsActive": True
  },
  {
    "Code": 200,
    "Link": "http://en.wikipedia.org/wiki/Animation",
    "IsActive": True
  },
  {
    "Code": 201,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh781237.aspx",
    "IsActive": True
  },
  {
    "Code": 202,
    "Link": "https://developer.mozilla.org/en/CSS/transform",
    "IsActive": True
  },
  {
    "Code": 203,
    "Link": "http://oli.jp/2010/css-animatable-properties/",
    "IsActive": True
  },
  {
    "Code": 204,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh465424.aspx",
    "IsActive": True
  },
  {
    "Code": 205,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh465165.aspx",
    "IsActive": True
  },
  {
    "Code": 206,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh465415.aspx ",
    "IsActive": True
  },
  {
    "Code": 207,
    "Link": "http://msdn.microsoft.com/en-US/library/windows/apps/hh465415.aspx#touch_targets ",
    "IsActive": True
  },
  {
    "Code": 208,
    "Link": "http://msdn.microsoft.com/en-US/library/windows/apps/hh465415.aspx",
    "IsActive": True
  },
  {
    "Code": 209,
    "Link": "http://msdn.microsoft.com/en-US/library/windows/apps/hh465415.aspx",
    "IsActive": True
  },
  {
    "Code": 210,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh761499.aspx",
    "IsActive": True
  },
  {
    "Code": 211,
    "Link": "http://msdn.microsoft.com/en-US/library/windows/apps/hh465415.aspx",
    "IsActive": True
  },
  {
    "Code": 212,
    "Link": "http://visualstudiogallery.msdn.microsoft.com/bb764f67-6b2c-4e14-b2d3-17477ae1eaca?SRC=Featured",
    "IsActive": True
  },
  {
    "Code": 213,
    "Link": "http://www.digikey.com/scripts/DkSearch/dksus.dll?lang=en&keywords=STEVAL-MKI119V1&x=18&y=18&cur=USD",
    "IsActive": True
  },
  {
    "Code": 214,
    "Link": "http://www.st.com/internet/evalboard/product/252756.jsp",
    "IsActive": True
  },
  {
    "Code": 215,
    "Link": "http://en.wikipedia.org/wiki/Lux",
    "IsActive": True
  },
  {
    "Code": 216,
    "Link": "http://appdev.windows.com ",
    "IsActive": True
  },
  {
    "Code": 217,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh694081.aspx ",
    "IsActive": True
  },
  {
    "Code": 218,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh694081.aspx ",
    "IsActive": True
  },
  {
    "Code": 219,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh694070.aspx",
    "IsActive": True
  },
  {
    "Code": 220,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh694069.aspx",
    "IsActive": True
  },
  {
    "Code": 221,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh694083.aspx",
    "IsActive": True
  },
  {
    "Code": 222,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh694083.aspx#acr_5_0",
    "IsActive": True
  },
  {
    "Code": 223,
    "Link": "http://advertising.microsoft.com/windowsadvertising/developer",
    "IsActive": True
  },
  {
    "Code": 224,
    "Link": "http://msdn.microsoft.com/en-us/library/hh506361(v=msads.10).aspx",
    "IsActive": True
  },
  {
    "Code": 225,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh924350.aspx",
    "IsActive": True
  },
  {
    "Code": 226,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh846296.aspx#promoimages",
    "IsActive": True
  },
  {
    "Code": 227,
    "Link": "http://www.w3.org/TR/html401/",
    "IsActive": True
  },
  {
    "Code": 228,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh767420.aspx",
    "IsActive": True
  },
  {
    "Code": 229,
    "Link": "http://dev.w3.org/html5/2dcontext/",
    "IsActive": True
  },
  {
    "Code": 230,
    "Link": "http://www.w3.org/TR/SVG/",
    "IsActive": True
  },
  {
    "Code": 231,
    "Link": "http://www.w3.org/TR/html5/global-attributes.html#embedding-custom-non-visible-data-with-the-data-attributes",
    "IsActive": True
  },
  {
    "Code": 232,
    "Link": "http://html5.validator.nu/",
    "IsActive": True
  },
  {
    "Code": 233,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/Hh996830.aspx ",
    "IsActive": True
  },
  {
    "Code": 234,
    "Link": "http://css-tricks.com/category/advanced/",
    "IsActive": True
  },
  {
    "Code": 235,
    "Link": "http://css-tricks.com/pseudo-class-selectors/",
    "IsActive": True
  },
  {
    "Code": 236,
    "Link": "http://tools.css3.info/selectors-test/test.html ",
    "IsActive": True
  },
  {
    "Code": 237,
    "Link": "http://ecma-international.org/publications/standards/Ecma-335.htm",
    "IsActive": True
  },
  {
    "Code": 238,
    "Link": "http://msdn.microsoft.com/en-us/library/b272f386(v=vs.94)",
    "IsActive": True
  },
  {
    "Code": 239,
    "Link": "http://msdn.microsoft.com/en-us/library/cd9w2te4(v=vs.94)",
    "IsActive": True
  },
  {
    "Code": 240,
    "Link": "http://msdn.microsoft.com/en-us/library/h6e2eb7w(v=VS.94).aspx",
    "IsActive": True
  },
  {
    "Code": 241,
    "Link": "http://msdn.microsoft.com/en-us/library/k4h76zbx(v=vs.94)",
    "IsActive": True
  },
  {
    "Code": 242,
    "Link": "http://www.sellsbrothers.com/posts/Details/12692",
    "IsActive": True
  },
  {
    "Code": 243,
    "Link": "http://msdn.microsoft.com/en-us/library/br230269(v=VS.94).aspx",
    "IsActive": True
  },
  {
    "Code": 244,
    "Link": "http://msdn.microsoft.com/en-us/library/dd492638.aspx",
    "IsActive": True
  },
  {
    "Code": 245,
    "Link": "http://www.w3.org/TR/2011/WD-html5-20110525/",
    "IsActive": True
  },
  {
    "Code": 246,
    "Link": "http://msdn.microsoft.com/en-us/library/hh768146(v=vs.110).aspx",
    "IsActive": True
  },
  {
    "Code": 247,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/br205768.aspx",
    "IsActive": True
  },
  {
    "Code": 248,
    "Link": "http://msdn.microsoft.com/en-us/library/cc836458(v=VS.94).aspx",
    "IsActive": True
  },
  {
    "Code": 249,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/Hh770544.aspx",
    "IsActive": True
  },
  {
    "Code": 250,
    "Link": "http://code.msdn.microsoft.com/windowsapps/Splash-screen-sample-89c1dc78",
    "IsActive": True
  },
  {
    "Code": 251,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh452684.aspx",
    "IsActive": True
  },
  {
    "Code": 252,
    "Link": "http://blogs.msdn.com/b/b8/archive/2011/09/28/extending-quot-windows-8-quot-apps-to-the-cloud-with-skydrive.aspx",
    "IsActive": True
  },
  {
    "Code": 253,
    "Link": "http://code.msdn.microsoft.com/windowsapps/File-picker-sample-9f294cba",
    "IsActive": True
  },
  {
    "Code": 254,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/Hh770544.aspx",
    "IsActive": True
  },
  {
    "Code": 255,
    "Link": "http://code.msdn.microsoft.com/windowsapps/Splash-screen-sample-89c1dc78",
    "IsActive": True
  },
  {
    "Code": 256,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh452684.aspx",
    "IsActive": True
  },
  {
    "Code": 257,
    "Link": "http://blogs.msdn.com/b/b8/archive/2011/09/28/extending-quot-windows-8-quot-apps-to-the-cloud-with-skydrive.aspx",
    "IsActive": True
  },
  {
    "Code": 258,
    "Link": "http://code.msdn.microsoft.com/windowsapps/File-picker-sample-9f294cba",
    "IsActive": True
  },
  {
    "Code": 259,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh923025.aspx",
    "IsActive": True
  },
  {
    "Code": 260,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/Hh758299.aspx",
    "IsActive": True
  },
  {
    "Code": 261,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh771179.aspx",
    "IsActive": True
  },
  {
    "Code": 262,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/windows.ui.notifications.tiletemplatetype.aspx",
    "IsActive": True
  },
  {
    "Code": 263,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/windows.ui.notifications.tileupdater.startperiodicupdate.aspx",
    "IsActive": True
  },
  {
    "Code": 264,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh761458.aspx",
    "IsActive": True
  },
  {
    "Code": 265,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh977046.aspx",
    "IsActive": True
  },
  {
    "Code": 266,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/windows.applicationmodel.background.systemconditiontype.aspx",
    "IsActive": True
  },
  {
    "Code": 267,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh767434.aspx",
    "IsActive": True
  },
  {
    "Code": 268,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/windows.applicationmodel.background.systemtriggertype",
    "IsActive": True
  },
  {
    "Code": 269,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/windows.ui.notifications.toasttemplatetype.aspx",
    "IsActive": True
  },
  {
    "Code": 270,
    "Link": "http://code.msdn.microsoft.com/windowsapps/Toast-notifications-sample-52eeba29",
    "IsActive": True
  },
  {
    "Code": 271,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh464936.aspx",
    "IsActive": True
  },
  {
    "Code": 272,
    "Link": "http://code.msdn.microsoft.com/windowsapps/Network-Information-Sample-63aaa201",
    "IsActive": True
  },
  {
    "Code": 273,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/br229787.aspx",
    "IsActive": True
  },
  {
    "Code": 274,
    "Link": "http://en.wikipedia.org/wiki/Rss",
    "IsActive": True
  },
  {
    "Code": 275,
    "Link": "http://www.ietf.org/rfc/rfc4287.txt",
    "IsActive": True
  },
  {
    "Code": 276,
    "Link": "http://msdn.microsoft.com/en-US/library/windows/apps/hh913756",
    "IsActive": True
  },
  {
    "Code": 277,
    "Link": "http://code.msdn.microsoft.com/windowsapps/Background-Transfer-Sample-d7833f61",
    "IsActive": True
  },
  {
    "Code": 278,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh441129.aspx",
    "IsActive": True
  },
  {
    "Code": 279,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh465373%28v=VS.85%29.aspx",
    "IsActive": True
  },
  {
    "Code": 280,
    "Link": "http://msdn.microsoft.com/en-us/library/ie/cc197015(v=vs.85).aspx",
    "IsActive": True
  },
  {
    "Code": 281,
    "Link": "http://documentcloud.github.com/underscore/docs/underscore.html",
    "IsActive": True
  },
  {
    "Code": 282,
    "Link": "http://msdn.microsoft.com/en-US/library/windows/apps/br211385",
    "IsActive": True
  },
  {
    "Code": 283,
    "Link": "http://msdn.microsoft.com/en-US/library/windows/apps/br211385",
    "IsActive": True
  },
  {
    "Code": 284,
    "Link": "http://msdn.microsoft.com/en-us/library/ms745109.aspx",
    "IsActive": True
  },
  {
    "Code": 285,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh465149.aspx",
    "IsActive": True
  },
  {
    "Code": 286,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/hh465415.aspx",
    "IsActive": True
  },
  {
    "Code": 287,
    "Link": "http://technet.microsoft.com/en-us/library/hh852635.aspx",
    "IsActive": True
  },
  {
    "Code": 288,
    "Link": "http://msdn.microsoft.com/en-us/library/windows/apps/jj193598.aspx",
    "IsActive": True
  },
  {
    "Code": 289,
    "Link": "http://www.sellsbrothers.com/Posts/Details/999999",
    "IsActive": True
  }
]

class MainPage(webapp2.RequestHandler):
    def get(self, codeStr):
      try:
        code = int(codeStr)
        link = [r["Link"] for r in redirects if r["Code"] == code][0]
        #self.response.write(link)
        return self.redirect(link)
      except:
        #self.abort(404)
        self.response.write(open( 'home.html', 'r' ).read())

app = webapp2.WSGIApplication([
    (r'/(\d+)', MainPage),
], debug=True)











