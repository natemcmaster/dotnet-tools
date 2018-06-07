# dotnet-tools

A list of tool extensions for .NET Core Command Line (dotnet CLI).

## DotNet tools (aka global tools)

These tools can be installed by executing

    dotnet tool install -g <package id>

> Pro-tip: global tools do not need to be named "dotnet-*". This is only a convention used some authors as a way to indicate a package is meant to be a command line tool, and not a normal library reference.

<!-- CONTRIBUTORS: please add to the list alphabetically, ignoring the `dotnet-` prefix. -->

Name | Author | Description
-----|--------|--------------
[dotnet-certes](https://github.com/fszlin/certes) | [@fszlin](https://github.com/fszlin) | CLI tool for acquire certificates via the Automated Certificate Management Environment (ACME) protocol (example: LetsEncrypt.org) [NuGet](https://www.nuget.org/packages/dotnet-certes/)
[dotnet-doc](https://github.com/spboyer/dotnet-doc) | [@spboyer](https://github.com/spboyer) | Search [docs.microsoft.com](https://docs.microsoft.com) using the command line. [NuGet](https://www.nuget.org/packages/dotnet-doc/)
[git-status-cli](https://github.com/jerriep/git-status-cli) | [@jerriep](https://github.com/jerriep) | A simple command-line utility to determine status of all Git repositories in a directory structure. [NuGet](https://www.nuget.org/packages/git-status-cli/)
[github-issues-cli](https://github.com/jerriep/github-issues-cli) | [@jerriep](https://github.com/jerriep) | A simple command-line client for managing GitHub Issues. [NuGet](https://www.nuget.org/packages/github-issues-cli/)
[localappveyor](https://github.com/joaope/localappveyor) | [@joaope](https://github.com/joaope) | .NET Core global tool which brings appveyor.yml to the center of your build process by making possible to execute its build jobs, locally.
[dotnet-md5](https://github.com/Rwing/Dotnet.Tool.MD5) | [@Rwing](https://github.com/Rwing) | Just generate MD5 hash value in CLI. [NuGet](https://www.nuget.org/packages/dmd5)
[nuke](https://github.com/nuke-build/nuke) | [@nuke-build](https://github.com/nuke-build) | Run and setup NUKE builds with a single command on any platform :rocket: [NuGet](https://www.nuget.org/packages/Nuke.GlobalTool)
[NuKeeper](https://github.com/NuKeeperDotNet/NuKeeper) | [@AnthonySteele](https://github.com/anthonysteele) | Find outdated NuGet packages and apply updates to them. [NuGet](https://www.nuget.org/packages/NuKeeper)
[nyancat](https://github.com/nickvdyck/nyancat.cs) | [@nickvdyck](https://github.com/nickvdyck) | Nyancat 😻 in your terminal, rendered through ANSI escape sequences. A port of the orignal terminal application to make this cat run on dotnet core. 🐱‍🏍 [Nuget](https://www.nuget.org/packages/nyancat/)
[dotnet-outdated](https://github.com/jerriep/dotnet-outdated) | [@jerriep](https://github.com/jerriep) | A .NET Core global tool to display outdated NuGet packages in a project. [NuGet](https://www.nuget.org/packages/dotnet-outdated/)
[protogen](https://github.com/mgravell/protobuf-net) | [@mgravell](https://github.com/mgravell) | protobuf-net code-generation from .proto schema files
[dotnetrsa](https://github.com/stulzq/DotnetRSA) | [@stulzq](https://github.com/stulzq) | Generate rsa pkcs1, pkcs8, xml format key. Conversion between the three formats. [NuGet](https://www.nuget.org/packages/dotnetrsa)
[dotnet-script](https://github.com/filipw/dotnet-script) | [@filipw](https://github.com/filipw) [@seesharper](https://github.com/seesharper) | Run C# scripts from the .NET CLI. [NuGet](https://www.nuget.org/packages/dotnet-script/)
[dotnet-search](https://github.com/billpratt/dotnet-search) | [@billpratt](https://github.com/billpratt) | Search for Nuget packages using the .NET Core CLI. [NuGet](https://www.nuget.org/packages/dotnet-search/)
[dotnet-serve](https://github.com/natemcmaster/dotnet-serve) | [@natemcmaster](https://github.com/natemcmaster) | A simple command line HTTP server, not code required. [NuGet](https://www.nuget.org/packages/dotnet-serve/)
[sleet](https://github.com/emgarten/Sleet) | [@emgarten](https://github.com/emgarten) | A static NuGet feed generator.  [NuGet](https://www.nuget.org/packages/Sleet/)
[srihash-cli](https://github.com/natemcmaster/srihash-cli) | [@natemcmaster](https://github.com/natemcmaster) | Generates the SRI hash for `<script>` tags in browsers [NuGet](https://nuget.org/packages/srihash-cli)
[weeknumber](https://github.com/MarkusLund/weeknumber) | [@MarkusLund](MarkusLund) | Prints the current weeknumber to the command line. [NuGet](https://nuget.org/packages/weeknumber/)
[dotnet-xdt](https://github.com/nil4/dotnet-transform-xdt) | [@nil4](https://github.com/nil4) | Global tool for applying XML Document Transformations to .NET configuration files, or any other XML-structured content. [NuGet](https://www.nuget.org/packages/dotnet-xdt/)

## DotNetCliToolRef tools (aka project-only tools)

These tools can only be installed by adding `<DotNetCliToolReference>` into your MSBuild project file.

### Official

Tools created by companies and organizations.

Name | Author | Description
-----|--------|--------------
[dotnet-compile-php](https://github.com/iolevel/peachpie) | iolevel | Command line for [Peachpie](http://www.peachpie.io/) - the PHP Compiler and Runtime for .NET [NuGet](https://www.nuget.org/packages/Peachpie.Compiler.Tools/)
[dotnet-git-commit-hash](https://github.com/bitcraftCoLtd/GitCommitHash) | bitcraft Co., Ltd. | Tool that generates a C# source code file making the latest git commit hash available at runtime. [NuGet](https://www.nuget.org/packages/Bitcraft.Tools.GitCommitHash/)
[dotnet-lambda](https://github.com/aws/aws-extensions-for-dotnet-cli) | Amazon | Tools to deploy AWS Lambda functions. [NuGet](https://www.nuget.org/packages/Amazon.Lambda.Tools)
[dotnet-ecs](https://github.com/aws/aws-extensions-for-dotnet-cli) | Amazon | Tools to deploy containers to Amazon Elastic Container Service functions. [NuGet](https://www.nuget.org/packages/Amazon.ECS.Tools)
[dotnet-eb](https://github.com/aws/aws-extensions-for-dotnet-cli) | Amazon | Tools to deploy ASP.NET Core apps to AWS Elastic Beanstalk. [NuGet](https://www.nuget.org/packages/Amazon.ElasticBeanstalk.Tools)
[dotnet-nanopack](https://github.com/OctopusDeploy/NanoPack) | OctopusDeploy | A tool to package ASP.NET Core applications into a NanoServer VHD. [NuGet](https://www.nuget.org/packages/NanoPack/)
[dotnet-proto](https://github.com/WhereIsMyTransport/dotnetcli-proto-tool) | WhereIsMyTransport | A tool to assist with compiling and versioning Google Protobuf schema files. [NuGet](https://www.nuget.org/packages/WhereIsMyTransport.Protobuf.Tools.Dotnet/)
[dotnet-xunit](https://github.com/xunit/xunit) | Xunit | A command-line runner for xunit.  [NuGet](https://www.nuget.org/packages/dotnet-xunit)

**Special mention**
These tools area available as packages for .NET Core CLI 1.x or 2.0. In the 2.1 CLI, these were made part of the CLI and do not need to be specially installed. See <https://github.com/aspnet/Announcements/issues/290>.

Name | Author | Description
-----|--------|--------------
[dotnet-ef](https://github.com/aspnet/EntityFramework.Tools) | Microsoft | Tools for Entity Framework Core [NuGet](https://www.nuget.org/packages/Microsoft.EntityFrameworkCore.Tools.DotNet/)
[dotnet-sql-cache](https://github.com/aspnet/DotNetTools) | Microsoft | Initializes a MSSQL database with tables for use with Microsoft.Extensions.Caching.SqlServer. [NuGet](https://www.nuget.org/packages/Microsoft.Extensions.Caching.SqlConfig.Tools)
[dotnet-user-secrets](https://github.com/aspnet/DotNetTools) | Microsoft | Tool for adding, removing and changing user secrets for use with Microsoft.Extensions.Configuration.UserSecrets [NuGet](https://www.nuget.org/packages/Microsoft.Extensions.SecretManager.Tools)
[dotnet-watch](https://github.com/aspnet/DotNetTools) | Microsoft | A .NET Core file watcher that triggers dotnet commands when a project or its files change [NuGet](https://www.nuget.org/packages/Microsoft.DotNet.Watcher.Tools)

### Community

Tools created by community members.

Name | Description
-----|------------
[dotnet-autover](https://github.com/f14shm4n/f14.AutoVersion) | A tool to auto update build version for your project. [NuGet](https://www.nuget.org/packages/f14.AutoVersion)
[dotnet-bolt](https://github.com/justkao/Bolt) | Tools for Bolt, a lean and lightweight WCF alternative library based on ASP.NET Core. [NuGet](https://www.nuget.org/packages/Bolt.Tools/)
[dotnet-bundle](https://github.com/madskristensen/BundlerMinifier) | BundlerMinifier.Core let's you configure bundling and minification of JS, CSS and HTML files. [NuGet](https://www.nuget.org/packages/BundlerMinifier)
[dotnet-clean](https://github.com/tsolarin/dotnet-clean) | DotNet.Cleaner.Tools is a tool for cleaning projects [NuGet](https://nuget.org/packages/DotNet.Cleaner.Tools)
[dotnet-commands](https://github.com/Lambda3/dotnet-commands) | A tool that allows you to use any executable as a .NET CLI Command, with special treatment for .NET Core apps. Follow [these instructions](https://github.com/Lambda3/dotnet-commands) to install.
[dotnet-dbupdate](https://github.com/prayzzz/UniversalDbUpdater) | A tool for managing scripts to backup and update MySQL and MSSQL databases [NuGet](https://www.nuget.org/packages/UniversalDbUpdater/)
[dotnet-docxml2md](https://github.com/Chida82/docxml2md) | A tool to converter .NET XML documentation into Markdown [NuGet](https://www.nuget.org/packages/docxml2md/)
[dotnet-fb](https://github.com/mczachurski/FluentBehave)  | FluentBehave is a simple framework to generate C# code base on Gherkin feature files. [NuGet](https://www.nuget.org/packages/FluentBehave.Tools)
[dotnet-fssrgen](https://github.com/fsprojects/FsSrGen) | F# String Response Generator [NuGet](https://www.nuget.org/packages/dotnet-fssrgen/)
[dotnet-gen](https://github.com/Muchiachio/Genny) | A code generator for dotnet projects [NuGet](https://www.nuget.org/packages/Genny/)
[dotnet-gitversion](https://github.com/nakioman/gitversioncore-tools) | Uses conventions to derive a SemVer product version from a GitFlow or GitHub based repository. [NuGet](https://www.nuget.org/packages/GitVersion.Tools/)
[dotnet-globwatch](https://github.com/mdschweda/globwatch) | GlobWatch is a .NET Core file system watcher that runs commands on changes. [NuGet](https://www.nuget.org/packages/GlobWatch/)
[dotnet-gplex](https://github.com/Oleg1cqa/gplex) | Tools for dotnet core based on Gardens Point LEX version 1.2.2 [NuGet](https://www.nuget.org/packages/StarodubOleg.GPLEX)
[dotnet-gppg](https://github.com/Oleg1cqa/gppg) | Adaptation of Gardens Point Parser Generator version 1.5.2 for dotnet core [NuGet](https://www.nuget.org/packages/StarodubOleg.GPPG/)
[dotnet-imgopt](https://github.com/anuraj/ImageOptimize) | ImageOptimize is a tool for image optimization. [NuGet](https://www.nuget.org/packages/imageoptimize/)
[dotnet-migrate](https://github.com/giggio/FluentMigrator.Runner.Cli) | A runner for [Fluent Migrator](https://github.com/schambers/fluentmigrator/). [NuGet](https://www.nuget.org/packages/FluentMigrator.Runner.Cli)
[dotnet-mono](https://github.com/TheAngryByrd/dotnet-mono) | Run applications targeting .net full framework with mono. [NuGet](https://www.nuget.org/packages/dotnet-mono/)
[dotnet-nswag](https://github.com/NSwag/NSwag) | Tools for NSwag, a Swagger 2.0 API for .NET, Web API, TypeScript. [NuGet](https://www.nuget.org/packages/NSwag.ConsoleCore/)
[dotnet-outdated](https://github.com/goenning/dotnet-outdated) | DotNetOutdated is a tool to check for outdated .NET Core dependencies. [NuGet](https://www.nuget.org/packages/DotNetOutdated/)
[dotnet-project-version](https://github.com/rwasef1830/ProjectVersioning.DotNet.Cli) | ProjectVersioning.DotNet.Cli is a project version generator tool [NuGet](https://www.nuget.org/packages/ProjectVersioning.DotNet.Cli/)
[dotnet-prop](https://github.com/simonech/dotnet-prop) | dotnet-cli tool for managing properties in netcore projects based on MSBuild. [NuGet](https://www.nuget.org/packages/dotnet-prop)
[dotnet-publish-ssh](https://github.com/albekov/dotnet-publish-ssh) | DotnetPublishSsh is a a tool to publish your .NET Core application to Linux server via SSH. [NuGet](https://www.nuget.org/packages/DotnetPublishSsh/)
[dotnet-swashbuckle](https://github.com/geeklearningio/gl-swashbuckle) | Swashbuckle extensions to add examples and security requirements in the generated Swagger file. [NuGet](https://www.nuget.org/packages/GeekLearning.DotNet.Swashbuckle)
[dotnet-transform-xdt](https://github.com/nil4/dotnet-transform-xdt) | XDT (XML Document Transform) publish tool for transforming XML files at publishing time. [NuGet](https://www.nuget.org/packages/Microsoft.DotNet.Xdt.Tools)
[dotnet-tsd](https://github.com/originalmoose/Typescript.Definitions.Tools) | Typescript.Definitions.Tools is a helper library to generate typescript definition files and typescript files from c# code. [NuGet](https://www.nuget.org/packages/Typescript.Definitions.Tools/)
[dotnet-tinify](https://github.com/andrewlock/dotnet-tinify) | A tool for squashing PNG and JPEG files using the [TinyPNG API](https://tinypng.com/developers). [NuGet](https://www.nuget.org/packages/dotnet-tinify/)
[dotnet-unpkg](https://github.com/rendlelabs/dotnet-unpkg) | A tool to install front-end packages from [unpkg.com](https://unpkg.com) with no need for Node.js/NPM/Yarn/whatever. [NuGet](https://www.nuget.org/packages/RendleLabs.UnpkgCli)
[dotnet-web-compile](https://github.com/sgjsakura/DotNetCore-WebCompiler) | A tool to compile client web files (e.g. SCSS, TS, etc). [NuGet](https://www.nuget.org/packages/Sakura.AspNetCore.Tools.WebCompiler/)

### Experimental

These tools are not yet available on NuGet.org.

Name | Description
-----|------------
[dotnet-cake](https://github.com/cake-build/frosting) | A stand-alone .NET Core runner and host for Cake. [MyGet gallery](https://www.myget.org/gallery/cake)
[dotnet-st](https://github.com/storyteller/Storyteller) | Storyteller is a tool for crafting executable specifications. *(Requires manual installation but is available on [NuGet](https://www.nuget.org/packages/Storyteller/)).*

## Wanted

These are tools that either exists in other ecosystems or are utilities that are in high demand that the community should consider building.

Description|node.js version|golang version|python version|other lang
-----------|---------------|--------------|--------------|----------
Give thanks to the open source maintainers you depend on| [thanks](https://www.npmjs.com/package/thanks)
