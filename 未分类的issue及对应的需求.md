## 从Issue到需求（未分类）

1. #109117：Editor tab shadow is rendered on top of contrast border

   需求：IDE的GUI界面应当简洁美观、操作流畅，开发人员应当修复GUI界面内部显示bug。

2. #109060：Without any editors open the find widget doesn't show in the Output pane

   需求：在未打开任何编辑器情况下，在输出栏中也应该显示查询窗口，以保证用户在未打开编辑器时也能搜索关键词。

3. #108868：onDidChangeActiveTextEditor fired twice when closing the editor

   需求：在用户使用快捷键关闭某一个编辑器窗口时，`onDidChangeActiveTextEditor`只应当被触发一次。

4. #109220：No didClose/didOpen event when rename Java file to different cases 

   需求：在对Java文件重命名时，应当分别对原来URI和新的URI触发didClose和didOpen事件。

5. #109044：The generated active file is shown in the root of workspace

   需求：用户生成的活动文件不应当被放置在工作区的根目录中，以便用户对于工作区进行管理。

6. #109196：Editor Tab Groups

   需求：在使用编辑器时，用户可以对标签进行分组管理。

7. #109131：vscode API - editors TextEditor.edit can control undo/redo stack

   需求：对于涉及editor的操作，可以实现撤销和恢复。

8. #109109：Terraform autoformatting stops working when in settings.json editor.formatOnSaveMode is set to a value

   需求：用户可以自定义编辑器的配置文件。

9. #108536："Editor: Accept Suggestion On Enter" should default to Off 

   需求：编辑器对于接受输入建议应当默认为关闭，不自动弹出。

10. #108515：Fixes Search in the search editor does not respect the modified sort field

    需求：在搜索功能中，搜索结果可以按照字段进行排序。

11. #109113：Have a setting option to close "(Working Tree)" tab when pressing "Open File"

    需求：更改设置时，可以在点击"Open File"时更改"(Working Tree)" 状态。

12. #109082：Terminals are reused across workspaces

    需求：终端应当可以跨工作区重复使用。

13. #108669：Offer to open workspace in root even when telemetry has been disabled and in web

    需求：在 telemetry功能关闭时，也能在根目录中使用工作区。

14. #108606：Search feature when using workspace is searching folders that should be ignored

    需求：在使用工作区的搜索功能时，应当能忽略部分文件夹。

15. #108495：Workspace doesn't preserve selected source control repositories

    需求：工作区可以保留选定的源代码控制仓库。

16. #108575：Window reloads when adding or removing folder from workspace

    需求：工作区添加或删除文件夹时，不应当重新加载窗口。

17. #108532：Ability to create a file with that uses a custom editor without needing to have an open workspace 

    需求：用户应当能够使用自定义编辑器创建文件，而无需具有打开的工作区。

18. #109144：Go to References does not work on staged files

    需求：暂存文件应当可以使用“ go to references ”功能。

19. #108670：Avoid the reload required for each change in the snippets.json file

    需求：可以避免每次更改`snippets.json`文件都需要重新加载。

20. #108295：To be able to accept all current/incoming changes when solving merge conflicts in a file

    需求：解决文件中的合并冲突时能够接受所有current/incoming状态的更改。

21. #108579：File is not active in tab when opened from search results

    需求：在搜索结果中打开文件时，文件应当处于活动状态。

22. #108497：Github/vscode icon should not reload editor

    需求：在点击Github/vscode图标时，不会重新加载编辑器。

23. #108358：Source Control file list is super hard to read

    需求：IDE的源代码文件可读性差，应当进行改进其可读性。

24. #109130：Extensions can add context value (metadata) to editors

    需求：插件能够将源文件一些元数据添加到文档中，用户使用快捷键运行程序时，IDE基于元数据执行不同的行为。例如，插件判断源文件中是否有main()方法，若有则运行该应用程序；插件判断源文件中是否有测试用例，若有则运行测试用例。

25. #109074：.NET test debugging extension path length restriction

    需求：使用.NET CORE测试调试时，IDE对于插件的路径名的最大值限制应当允许用户自行设定，否则会出现插件的路径名过长导致无法调试的现象。

26. #109607：Extensions - Improve notification dialog when installing an extension

    需求：在安装拓展程序时，确认安装的通知对话框中应当显示安装的插件列表。

27. #109023：Provide Button to Show Additional Detail When Extension Install or Update Fails

    需求：在插件安装或更新失败时，应当提供一个“显示详细信息”的选项。

28. #105564：please allow a filter on not installed extensions too

    需求：对于没有安装的插件，应当提供一个筛选器，以便用户查询特定类型的未安装的插件。

29. #104568：Add Education extension category

    需求：IDE应当为插件添加“教育”的类别。

30. #102509：Disable plugin update notification

    需求：IDE应当允许用户禁止接收插件的更新通知，以便用户在愿意使用旧版本插件的情况下不被更新通知打扰。

31. #101781：Custom grouping for plugins

    需求：IDE应当允许用户自行对插件进行分组，以方便用户管理大量插件。

32. #92858：Reduce header size of extension view

    需求：在插件选项卡中，应当减小插件标题占用的垂直空间。在已打开底部终端的情况下，插件标题占用大量垂直空间会导致显示插件内容的空间很少。

33. #108054：Watchlist Of Extensions

    需求：添加收藏插件的功能，以便用户在发现感兴趣的插件但是没有安装的情况下能够再次找到这个插件。

34. \#109451：Git: Add Git Cache Remover

    需求：应当添加Git缓存删除器，以便开发过大量使用Git的项目的用户清理Git缓存空间。

35. \#104999：please always show english tip in git menu even user chosing cjk display language

    需求：在通过插件改变IDE的语言的情况下，其Git模块应当仍然使用英语，否则会出现一些关于Git的名词的不妥当的翻译。

36. \#104845：Git: Add support to delete remote git tags using command palette

    需求：IDE应当支持使用命令行删远程Git标签。当前IDE只支持删除本地标签。

37. \#104838：Git: Clone to an alternate directory name

    需求：用户在git clone项目时，应当可以指定目录名称。

38. \#96264：Option to disable creation of a branch when a remote tracking branch is selected

    需求：用户在远程跟踪分支的情况下，应当禁用创建分支的选项。

39. \#94711：Git: Offer to show the entire git commit output, when it fails

    需求：用户git commit失败时，应当显示完整的git commit的输出信息。

40. \#93300：Git: After cloning and no folder is open, add option to open the folder automatically.

    需求：如果用户在git clone之后没有打开任何文件夹，应当提供一个选项，用户通过选择该选项来自动打开git clone的文件夹。

41. \#62751：Git: Provide task progress

    需求：在Git输出控制台中，应当显示Git进度的详细信息。

42. \#50090：Git: Support Co-Authored-By

    需求：IDE应当支持多个作者共同对git commit信息进行署名。

43. \#109224：Diff editor: show path as description

    需求：git diff编辑器应当在描述信息中显示资源的路径。

44. \#109235：Option to change the title of the integrated terminal in vscode?

    需求：用户可以选择使用终端、调试控制台、问题和输出的浮动窗口，以减少用户在不同窗口间来回切换的操作，方便用户利用大屏幕空间或者多个显示器。

45. \#10546：Tabs for integrated terminal

    需求：应当支持用户使用多个终端的选项卡，而不是默认的单个终端。

46. \#46696：Allow extensions to modify terminal environment variables

    需求：应当允许插件修改终端的环境变量，以方便用户在项目本地设置SDK路径。

47. \#14973：Set environment variable before starting a terminal

    需求：在启动终端之前，用户可以通过设置一个选项来设置环境变量。

48. \#52320：Search all files from Console

    需求：用户可以在终端中搜索所有文件。

49. \#56838：Provide a way to kill a task or terminal from the main menu

    需求：用户能够通过主菜单中的选项来终止当前终端。

50. \#78431：[Terminal] Support Fast Scrolling

    需求：终端应当支持快速滚动，用户在按住alt建的同时滚动鼠标滚轮，可以通过1次鼠标滚轮滚动在终端中滚动1000行。

51. \#30077：Integrated Terminal: add "Clear Console" button

    需求：应当在集成终端面板中添加“clear”按钮，用来清空终端的内容。当前IDE的集成终端面板只有“add”和“kill”两个按钮，用户无法通过界面按钮来清空终端内容。

52. \#79063：Expose terminal scroll position and allow extension change it

    需求：用户可以通过插件获取和控制终端的滚动位置。

53. \#76381：Allowing integrated terminal zoom by mouse scroll

    需求：用户可以通过鼠标滚动对集成终端进行缩放，以方便使用较小屏幕的用户使用集成终端。