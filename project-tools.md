# Project tools

A list of project-only tools. Unlike [global tools](./README.md), these tools can only be installed by adding `<DotNetCliToolReference>` into your MSBuild project file, and are only available in the project folder.

```xml
<ItemGroup>
  <DotNetCliToolReference Include="package id" Version="version" />
</ItemGroup>
```

To use them, run `dotnet restore`. After restore is done, these tools are available as new subcommands of `dotnet` when you execute the
command from the project directory.

> Pro-tip: these tools *must* be named dotnet-something. [Global tools](./README.md), on the other hand, do not need this prefix.

Name | Description
-----|--------------
[dotnet-altcover](https://www.nuget.org/packages/altcover.dotnet/) | Cross-platform code line and branch coverage tool-set for .net core/.net framework/mono
[dotnet-autover](https://github.com/f14shm4n/f14.AutoVersion) | A tool to auto update build version for your project. [NuGet](https://www.nuget.org/packages/f14.AutoVersion)
[dotnet-bolt](https://github.com/justkao/Bolt) | Tools for Bolt, a lean and lightweight WCF alternative library based on ASP.NET Core. [NuGet](https://www.nuget.org/packages/Bolt.Tools/)
[dotnet-bundle](https://github.com/madskristensen/BundlerMinifier) | BundlerMinifier.Core let's you configure bundling and minification of JS, CSS and HTML files. [NuGet](https://www.nuget.org/packages/BundlerMinifier)
[dotnet-certdump](https://github.com/secana/CertDump)| Dump signing certificates from a Portable Executable (PE) file. [NuGet](https://www.nuget.org/packages/CertDump/)
[dotnet-clean](https://github.com/tsolarin/dotnet-clean) | DotNet.Cleaner.Tools is a tool for cleaning projects [NuGet](https://nuget.org/packages/DotNet.Cleaner.Tools)
[dotnet-commands](https://github.com/Lambda3/dotnet-commands) | A tool that allows you to use any executable as a .NET CLI Command, with special treatment for .NET Core apps. Follow [these instructions](https://github.com/Lambda3/dotnet-commands) to install.
[dotnet-compile-php](https://github.com/iolevel/peachpie) | Command line for [Peachpie](http://www.peachpie.io/) - the PHP Compiler and Runtime for .NET [NuGet](https://www.nuget.org/packages/Peachpie.Compiler.Tools/)
[dotnet-csproj-to-2017](https://github.com/hvanbakel/CsprojToVs2017) | Tool for converting a pre VS2017 csproj file to the new package format. [NuGet](https://www.nuget.org/packages/Project2015To2017.Cli)
[dotnet-dbupdate](https://github.com/prayzzz/UniversalDbUpdater) | A tool for managing scripts to backup and update MySQL and MSSQL databases [NuGet](https://www.nuget.org/packages/UniversalDbUpdater/)
[dotnet-docxml2md](https://github.com/Chida82/docxml2md) | A tool to converter .NET XML documentation into Markdown [NuGet](https://www.nuget.org/packages/docxml2md/)
[dotnet-eb](https://github.com/aws/aws-extensions-for-dotnet-cli) | Tools to deploy ASP.NET Core apps to AWS Elastic Beanstalk.  Global tool after starting at version 3.0.0.[NuGet](https://www.nuget.org/packages/Amazon.ElasticBeanstalk.Tools)
[dotnet-ecs](https://github.com/aws/aws-extensions-for-dotnet-cli) | Tools to deploy containers to Amazon Elastic Container Service functions. Global tool after starting at version 3.0.0. [NuGet](https://www.nuget.org/packages/Amazon.ECS.Tools)
[dotnet-encrypto](https://github.com/tomchavakis/encrypto) | A tool to encrypt/decrypt folder or files using AES 256 .[Nuget](https://www.nuget.org/packages/dotnet-encrypto)
[dotnet-fake-cli](https://github.com/fsharp/FAKE) | F# make tool for running build.fsx files. [NuGet](https://www.nuget.org/packages/fake-cli/)
[dotnet-fb](https://github.com/mczachurski/FluentBehave)  | FluentBehave is a simple framework to generate C# code base on Gherkin feature files. [NuGet](https://www.nuget.org/packages/FluentBehave.Tools)
[dotnet-flubu](https://github.com/flubu-core/flubu.core) | Fluent Builder. A cross platform build automation tool for building projects and executing deployment scripts using C# code. [Nuget](https://www.nuget.org/packages/dotnet-flubu/)
[dotnet-fssrgen](https://github.com/fsprojects/FsSrGen) | F# String Response Generator [NuGet](https://www.nuget.org/packages/dotnet-fssrgen/)
[dotnet-gen](https://github.com/Muchiachio/Genny) | A code generator for dotnet projects [NuGet](https://www.nuget.org/packages/Genny/)
[dotnet-git-commit-hash](https://github.com/bitcraftCoLtd/GitCommitHash) | Tool that generates a C# source code file making the latest git commit hash available at runtime. [NuGet](https://www.nuget.org/packages/Bitcraft.Tools.GitCommitHash/)
[dotnet-gitversion](https://github.com/nakioman/gitversioncore-tools) | Uses conventions to derive a SemVer product version from a GitFlow or GitHub based repository. [NuGet](https://www.nuget.org/packages/GitVersion.Tools/)
[dotnet-globwatch](https://github.com/mdschweda/globwatch) | GlobWatch is a .NET Core file system watcher that runs commands on changes. [NuGet](https://www.nuget.org/packages/GlobWatch/)
[dotnet-gplex](https://github.com/Oleg1cqa/gplex) | Tools for dotnet core based on Gardens Point LEX version 1.2.2 [NuGet](https://www.nuget.org/packages/StarodubOleg.GPLEX)
[dotnet-gppg](https://github.com/Oleg1cqa/gppg) | Adaptation of Gardens Point Parser Generator version 1.5.2 for dotnet core [NuGet](https://www.nuget.org/packages/StarodubOleg.GPPG/)
[dotnet-imgopt](https://github.com/anuraj/ImageOptimize) | ImageOptimize is a tool for image optimization. [NuGet](https://www.nuget.org/packages/imageoptimize/)
[dotnet-lambda](https://github.com/aws/aws-extensions-for-dotnet-cli) | Tools to deploy AWS Lambda functions. Global tool after starting at version 3.0.0.[NuGet](https://www.nuget.org/packages/Amazon.Lambda.Tools)
[dotnet-migrate](https://github.com/giggio/FluentMigrator.Runner.Cli) | A runner for [Fluent Migrator](https://github.com/schambers/fluentmigrator/). [NuGet](https://www.nuget.org/packages/FluentMigrator.Runner.Cli)
[dotnet-mono](https://github.com/TheAngryByrd/dotnet-mono) | Run applications targeting .net full framework with mono. [NuGet](https://www.nuget.org/packages/dotnet-mono/)
[dotnet-nanopack](https://github.com/OctopusDeploy/NanoPack) | A tool to package ASP.NET Core applications into a NanoServer VHD. [NuGet](https://www.nuget.org/packages/NanoPack/)
[dotnet-nbench](https://github.com/petabridge/nbench) | A tool for running NBench performance tests [NuGet](https://www.nuget.org/packages/dotnet-nbench/)
[dotnet-nswag](https://github.com/NSwag/NSwag) | Tools for NSwag, a Swagger 2.0 API for .NET, Web API, TypeScript. [NuGet](https://www.nuget.org/packages/NSwag.ConsoleCore/)
[dotnet-outdated](https://github.com/goenning/dotnet-outdated) | DotNetOutdated is a tool to check for outdated .NET Core dependencies. [NuGet](https://www.nuget.org/packages/DotNetOutdated/)
[dotnet-project-version](https://github.com/rwasef1830/ProjectVersioning.DotNet.Cli) | ProjectVersioning.DotNet.Cli is a project version generator tool [NuGet](https://www.nuget.org/packages/ProjectVersioning.DotNet.Cli/)
[dotnet-prop](https://github.com/simonech/dotnet-prop) | dotnet-cli tool for managing properties in netcore projects based on MSBuild. [NuGet](https://www.nuget.org/packages/dotnet-prop)
[dotnet-proto](https://github.com/WhereIsMyTransport/dotnetcli-proto-tool) | A tool to assist with compiling and versioning Google Protobuf schema files. [NuGet](https://www.nuget.org/packages/WhereIsMyTransport.Protobuf.Tools.Dotnet/)
[dotnet-publish-ssh](https://github.com/albekov/dotnet-publish-ssh) | DotnetPublishSsh is a a tool to publish your .NET Core application to Linux server via SSH. [NuGet](https://www.nuget.org/packages/DotnetPublishSsh/)
[dotnet-swashbuckle](https://github.com/geeklearningio/gl-swashbuckle) | Swashbuckle extensions to add examples and security requirements in the generated Swagger file. [NuGet](https://www.nuget.org/packages/GeekLearning.DotNet.Swashbuckle)
[dotnet-tinify](https://github.com/andrewlock/dotnet-tinify) | A tool for squashing PNG and JPEG files using the [TinyPNG API](https://tinypng.com/developers). [NuGet](https://www.nuget.org/packages/dotnet-tinify/)
[dotnet-tools-outdated](https://github.com/rychlym/dotnet-tools-outdated) | Checks whether any of currently installed global tools is outdated. [NuGet](https://www.nuget.org/packages/dotnet-tools-outdated/)
[dotnet-transform-xdt](https://github.com/nil4/dotnet-transform-xdt) | XDT (XML Document Transform) publish tool for transforming XML files at publishing time. [NuGet](https://www.nuget.org/packages/Microsoft.DotNet.Xdt.Tools)
[dotnet-tsd](https://github.com/originalmoose/Typescript.Definitions.Tools) | Typescript.Definitions.Tools is a helper library to generate typescript definition files and typescript files from c# code. [NuGet](https://www.nuget.org/packages/Typescript.Definitions.Tools/)
[dotnet-t4-project-tool](https://github.com/mono/t4) | T4 text template processor. Project tool version of the `dotnet-t4` global tool package.
[dotnet-tt](https://github.com/atifaziz/t5) | T4 (Text Template Transformation Toolkit) for .NET Core
[dotnet-unpkg](https://github.com/rendlelabs/dotnet-unpkg) | A tool to install front-end packages from [unpkg.com](https://unpkg.com) with no need for Node.js/NPM/Yarn/whatever. [NuGet](https://www.nuget.org/packages/RendleLabs.UnpkgCli)
[dotnet-web-compile](https://github.com/sgjsakura/DotNetCore-WebCompiler) | A tool to compile client web files (e.g. SCSS, TS, etc). [NuGet](https://www.nuget.org/packages/Sakura.AspNetCore.Tools.WebCompiler/)
[dotnet-xunit](https://github.com/xunit/xunit) | A command-line runner for xunit.  [NuGet](https://www.nuget.org/packages/dotnet-xunit)

**Special mention**
These tools area available as packages for .NET Core CLI 1.x or 2.0. In the 2.1 CLI, these were made part of the CLI and do not
need to be specially installed. See <https://github.com/aspnet/Announcements/issues/290>.

Name | Description
-----|--------------
[dotnet-ef](https://github.com/aspnet/EntityFramework.Tools) | Tools for Entity Framework Core [NuGet](https://www.nuget.org/packages/Microsoft.EntityFrameworkCore.Tools.DotNet/)
[dotnet-sql-cache](https://github.com/aspnet/DotNetTools) | Initializes a MSSQL database with tables for use with Microsoft.Extensions.Caching.SqlServer. [NuGet](https://www.nuget.org/packages/Microsoft.Extensions.Caching.SqlConfig.Tools)
[dotnet-user-secrets](https://github.com/aspnet/DotNetTools) | Tool for adding, removing and changing user secrets for use with Microsoft.Extensions.Configuration.UserSecrets [NuGet](https://www.nuget.org/packages/Microsoft.Extensions.SecretManager.Tools)
[dotnet-watch](https://github.com/aspnet/DotNetTools) | A .NET Core file watcher that triggers dotnet commands when a project or its files change [NuGet](https://www.nuget.org/packages/Microsoft.DotNet.Watcher.Tools)
