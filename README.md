# dotnet-tools

A list of tool extensions for .NET Core Command Line (dotnet CLI).

These tools can be installed by executing

    dotnet tool install -g <package id>

> Pro-tip: global tools do not need to be named "dotnet-*". This is only a convention used some authors as a way to indicate a package is meant to be a command line tool, and not a normal library reference.

The CLI also supports an older format called "project tools" or `<DotNetCliToolReference>`. A list of project tools is [available here](./project-tools.md).

<!-- CONTRIBUTORS: please add to the list alphabetically, ignoring the `dotnet-` prefix. -->

Name | Author | Description
-----|--------|--------------
[dotnet-aop](https://github.com/ignatandrei/AOP_With_Roslyn)| [@ignatandrei](https://github.com/ignatandrei/) | A tool to make AOP for .cs files for your CI pipeline  . [NuGet](https://www.nuget.org/packages/dotnet-aop)
[dotnet-aspnet-codegenerator](https://github.com/aspnet/Scaffolding)| [@aspnet](https://github.com/aspnet)  | Code generation tool for creating controllers, views, and models in ASP.NET Core projects. [NuGet](https://www.nuget.org/packages/dotnet-aspnet-codegenerator/)
[dotnet-certes](https://github.com/fszlin/certes) | [@fszlin](https://github.com/fszlin) | CLI tool for acquire certificates via the Automated Certificate Management Environment (ACME) protocol (example: LetsEncrypt.org) [NuGet](https://www.nuget.org/packages/dotnet-certes/)
[dotnet-config2json](https://github.com/andrewlock/dotnet-config2json) | [@andrewlock](https://github.com/andrewlock/) | A simple tool to convert a web.config file to an appsettings.json file. [NuGet](https://www.nuget.org/packages/dotnet-config2json/)
[cowsay](https://github.com/isaac2004/dotnet-cowsay/) | [@isaac2004](https://github.com/isaac2004) |CLI Tool that gives a a random blog post from discoverdot.net in cowsay format. [NuGet](https://www.nuget.org/packages/dotnet-cowsay/)
[dotnet-dbinfo](https://github.com/berkid89/dotnet-dbinfo) | [@berkid89](https://github.com/berkid89) | A simple cross-platform command-line tool for get useful database information (in json format). [NuGet](https://www.nuget.org/packages/dotnet-dbinfo/)
[dotnet-doc](https://github.com/spboyer/dotnet-doc) | [@spboyer](https://github.com/spboyer) | Search [docs.microsoft.com](https://docs.microsoft.com) using the command line. [NuGet](https://www.nuget.org/packages/dotnet-doc/)
[docker-watch](https://github.com/nickvdyck/docker-watch) | [@nickvdyck](https://github.com/nickvdyck) | A command line utiltiy to notify docker mounted volumes about changes on Windows. [Nuget](https://www.nuget.org/packages/docker-watch)
[FlubuCore](https://github.com/flubu-core/flubu.core) | [@FlubuCore](https://github.com/flubu-core) | Fluent Builder. A cross platform build automation tool for building projects and executing deployment scripts using C# code. [Nuget](https://www.nuget.org/packages/FlubuCore.GlobalTool)
[git-status-cli](https://github.com/jerriep/git-status-cli) | [@jerriep](https://github.com/jerriep) | A simple command-line utility to determine status of all Git repositories in a directory structure. [NuGet](https://www.nuget.org/packages/git-status-cli/)
[github-issues-cli](https://github.com/jerriep/github-issues-cli) | [@jerriep](https://github.com/jerriep) | A simple command-line client for managing GitHub Issues. [NuGet](https://www.nuget.org/packages/github-issues-cli/)
[html-copy-vscode](https://github.com/slang25/html-copy-vscode) | [@slang25](https://github.com/slang25/) | A global tool to convert snippets copied from VS Code into plain html to paste into your blog. [NuGet](https://www.nuget.org/packages/HtmlCopyVSCode/)
[dotnet-ignore](https://github.com/Arasz/dotnet-ignore) | [@Arasz](https://github.com/Arasz) | Global .NET Core tool that can download .gitignore file from github gitignore repository. [NuGet](https://www.nuget.org/packages/dotnet-ignore/1.0.3)
[localappveyor](https://github.com/joaope/localappveyor) | [@joaope](https://github.com/joaope) | .NET Core global tool which brings appveyor.yml to the center of your build process by making possible to execute its build jobs, locally.
[dotnet-md5](https://github.com/Rwing/Dotnet.Tool.MD5) | [@Rwing](https://github.com/Rwing) | Just generate MD5 hash value in CLI. [NuGet](https://www.nuget.org/packages/dmd5)
[nuke](https://github.com/nuke-build/nuke) | [@nuke-build](https://github.com/nuke-build) | Run and setup NUKE builds with a single command on any platform :rocket: [NuGet](https://www.nuget.org/packages/Nuke.GlobalTool)
[NuKeeper](https://github.com/NuKeeperDotNet/NuKeeper) | [@AnthonySteele](https://github.com/anthonysteele) | Find outdated NuGet packages and apply updates to them. [NuGet](https://www.nuget.org/packages/NuKeeper)
[nyancat](https://github.com/nickvdyck/nyancat.cs) | [@nickvdyck](https://github.com/nickvdyck) | Nyancat 😻 in your terminal, rendered through ANSI escape sequences. A port of the orignal terminal application to make this cat run on dotnet core. 🐱‍🏍 [Nuget](https://www.nuget.org/packages/nyancat/)
[dotnet-outdated](https://github.com/jerriep/dotnet-outdated) | [@jerriep](https://github.com/jerriep) | A .NET Core global tool to display outdated NuGet packages in a project. [NuGet](https://www.nuget.org/packages/dotnet-outdated/)
[protogen](https://github.com/mgravell/protobuf-net) | [@mgravell](https://github.com/mgravell) | protobuf-net code-generation from .proto schema files
[RendleLabs.UnpkgCli](https://github.com/RendleLabs/dotnet-unpkg) | [@markrendle](https://github.com/markrendle) | Front-end package manager that uses the [unpkg.com](https://unpkg.com) CDN as a source. No Node.js, NPM or Bower required. [NuGet](https://www.nuget.org/packages/RendleLabs.UnpkgCli)
[dotnet-reportgenerator](https://github.com/danielpalme/ReportGenerator/) | [@danielpalme](https://github.com/danielpalme) | ReportGenerator converts XML reports generated by OpenCover, PartCover, dotCover, Visual Studio, NCover or Cobertura into human readable reports in various formats. [NuGet](https://www.nuget.org/packages/dotnet-reportgenerator-globaltool)
[dotnet-rider-cli](https://github.com/RendleLabs/dotnet-rider-cli/) | [@markrendle](https://github.com/markrendle) | **Windows only** Adds a `rider` command to launch JetBrains Rider when it's installed via [Toolbox](https://www.jetbrains.com/toolbox/). [NuGet](https://www.nuget.org/packages/dotnet-rider-cli)
[dotnetrsa](https://github.com/stulzq/DotnetRSA) | [@stulzq](https://github.com/stulzq) | Generate rsa pkcs1, pkcs8, xml format key. Conversion between the three formats. [NuGet](https://www.nuget.org/packages/dotnetrsa)
[dotnet-script](https://github.com/filipw/dotnet-script) | [@filipw](https://github.com/filipw) [@seesharper](https://github.com/seesharper) | Run C# scripts from the .NET CLI. [NuGet](https://www.nuget.org/packages/dotnet-script/)
[dotnet-search](https://github.com/billpratt/dotnet-search) | [@billpratt](https://github.com/billpratt) | Search for Nuget packages using the .NET Core CLI. [NuGet](https://www.nuget.org/packages/dotnet-search/)
[dotnet-serve](https://github.com/natemcmaster/dotnet-serve) | [@natemcmaster](https://github.com/natemcmaster) | A simple command line HTTP server, not code required. [NuGet](https://www.nuget.org/packages/dotnet-serve/)
[sleet](https://github.com/emgarten/Sleet) | [@emgarten](https://github.com/emgarten) | A static NuGet feed generator.  [NuGet](https://www.nuget.org/packages/Sleet/)
[dotnet-sonarscanner](https://github.com/SonarSource/sonar-scanner-msbuild) | [@SonarSource](https://github.com/SonarSource) | The SonarScanner for MSBuild is the recommended way to launch a SonarQube or SonarCloud analysis for projects/solutions using dotnet command as build tool. [NuGet](https://www.nuget.org/packages/dotnet-sonarscanner)
[dotnet-sshdeploy](https://github.com/unosquare/sshdeploy) | [@Unosquare](https://github.com/unosquare) | A dotnet CLI command that enables quick deployments over SSH. [NuGet](https://www.nuget.org/packages/dotnet-sshdeploy)
[srihash-cli](https://github.com/natemcmaster/srihash-cli) | [@natemcmaster](https://github.com/natemcmaster) | Generates the SRI hash for `<script>` tags in browsers [NuGet](https://nuget.org/packages/srihash-cli)
[weeknumber](https://github.com/MarkusLund/weeknumber) | [@MarkusLund](https://github.com/MarkusLund) | Prints the current weeknumber to the command line. [NuGet](https://nuget.org/packages/weeknumber/)
[dotnet-xdt](https://github.com/nil4/dotnet-transform-xdt) | [@nil4](https://github.com/nil4) | Global tool for applying XML Document Transformations to .NET configuration files, or any other XML-structured content. [NuGet](https://www.nuget.org/packages/dotnet-xdt/)
[dotnet-xscgen](https://github.com/mganss/XmlSchemaClassGenerator) | [@mganss](https://github.com/mganss) | Generate XmlSerializer compatible C# classes from XML Schema files. [NuGet](https://www.nuget.org/packages/dotnet-xscgen/)

<!-- CONTRIBUTORS: please add to the list alphabetically, ignoring the `dotnet-` prefix. -->

## Wanted

These are tools that either exists in other ecosystems or are utilities that are in high demand that the community should consider building.

Description|node.js version|golang version|python version|other lang
-----------|---------------|--------------|--------------|----------
Give thanks to the open source maintainers you depend on| [thanks](https://www.npmjs.com/package/thanks)
