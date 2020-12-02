# dotnet-tools

A list of tool extensions for .NET Core Command Line (dotnet CLI), aka '.NET Core global tools'.

## New!

NuGet.org now supports searching by package type. Find the complete list .NET tools here:

<a href="https://www.nuget.org/packages?packagetype=dotnettool" class="btn btn-primary btn-large">Go to .NET tools on NuGet.org</a>

## Unofficial list

The following list was created by users like you. Feel free to add yours. The presence of a tool in this list is not a recommendation of its quality or reliability.


> **Tip:** :bulb:
> Global tools do not need to be named "dotnet-*". This is only a convention used by some authors as a way to indicate a package is meant to be used as part of the `dotnet` command line tool, and not a standalone tool or library reference.

<table>
  <thead>
    <tr>
      <th>Command</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>aistdoc</code></td>
      <td>
        <p>
          Generates an API reference documentation for .NET and TypeScript code (based on XML Docs or TypeDoc comments) and publishes
          it on the web.
        </p>
        <p>
          <strong>Author:</strong> <a href="https://github.com/korzh">@korzh</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/Aistant.DocImport/">Aistant.DocImport</a></code>
      </td>
    </tr>
    <tr>
      <td><code>altcover</code></td>
      <td>
        <p>
          Cross-platform code line and branch coverage tool-set for .net core/.net framework/mono
        </p>
        <p>
          <strong>Author:</strong> <a href="https://github.com/SteveGilham">@SteveGilham</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/altcover.global/">altcover.global</a></code>
      </td>
    </tr>
    <tr>
      <td><code>altcover.visualizer</code></td>
      <td>
        <p>
          Code coverage display tool to show which parts of your code _aren't_ being covered. Requires GTK+3
          installed separately
        </p>
        <p>
          <strong>Author:</strong> <a href="https://github.com/SteveGilham">@SteveGilham</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/altcover.visualizer/">altcover.visualizer</a></code>
      </td>
    </tr>
    <tr>
      <td><code>as-cli</code></td>
      <td>
        <p>
          Use Azure Storage on CLI. Download, upload, show and more on CLI
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/peacecwz/azure-storage-cli">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/peacecwz">@peacecwz</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/azure-storage-cli/">azure-storage-cli</a></code>
      </td>
    </tr>
    <tr>
      <td><code>assembly-differ</code></td>
      <td>
        <p>
          Compare and Diff assemblies from different sources (inluding NuGet). Useful for determining what changes are introduced across versions, and if any are breaking.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/nullean/assembly-differ">GitHub</a>
          <br />
          <strong>Authors:</strong> <a href="https://github.com/orgs/nullean/people">Nullean commiters</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/assembly-differ/">assembly-differ</a></code>
      </td>
    </tr>
    <tr>
      <td><code>assembly-rewriter</code></td>
      <td>
        <p>
          Rewrites .NET assemblies with Mono.Cecil, to allow two different versions of the same assembly to be referenced within an application.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/nullean/assembly-rewriter">GitHub</a>
          <br />
          <strong>Authors:</strong> <a href="https://github.com/orgs/nullean/people">Nullean commiters</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/assembly-rewriter/">assembly-rewriter</a></code>
      </td>
    </tr>
    <tr>
      <td><code>autocommit</code></td>
      <td>
        <p>
          Automatically commit changes to git on a set interval, ending with a squash merge to the original head
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/StevenThuriot/GitAutoCommit">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/StevenThuriot/GitAutoCommit">@StevenThuriot</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-autocommit/">dotnet-autocommit</a></code>
      </td>
    </tr>
    <tr>
      <td><code>aver</code></td>
      <td>
        <p>
          Dotnet tool for reading assembly information
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/mocosha/assembly-version">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/mocosha">@mocosha</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/aver/">aver</a></code>
      </td>
    </tr>
    <tr>
      <td><code>az-lazy</code></td>
      <td>
        <p>
          Az Lazy CLI tool is designed for developers, it provides a command-line interface to quickly manage and make changes to azure storage queues, blobs and tables. 
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/faesel/az-lazy">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/faesel/">@faesel</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/az-lazy/">az-lazy</a></code>
      </td>
    </tr>
    <tr>
      <td><code>azure-boards-workitems</code></td>
      <td>
        <p>
          Execute queries and other work item data extraction tools.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/sep/AzDevWorkItemHistory">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/jonfuller">@jonfuller</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/azure-boards-workitems/">azure-boards-workitems</a></code>
      </td>
    </tr>
    <tr>
      <td><code>azuresigntool</code></td>
      <td>
        <p>
          Code sign your files using an Authenticode certificate stored in Azure Key Vault
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/vcsjones/AzureSignTool">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/vcsjones">@vcsjones</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/AzureSignTool/">azuresigntool</a></code>
      </td>
    </tr>
    <tr>
      <td><code>base64urls </code></td>
      <td>
        <p>
          CLI tool for base64 & base64url encode/decode for URL applications.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/guitarrapc/Base64UrlCore">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/guitarrapc">@guitarrapc</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/base64urls/">base64urls</a></code>
      </td>
    </tr>
    <tr>
      <td><code>benchmark</code></td>
      <td>
        <p>
          Provides a convenient way to execute your benchmark(s) from the command line interface.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/dotnet/BenchmarkDotNet">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/dotnet/BenchmarkDotNet">.NET Foundation and contributors</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/BenchmarkDotNet.Tool">BenchmarkDotNet.Tool</a></code>
      </td>
    </tr>
    <tr>
      <td><code>boots</code></td>
      <td>
        <p>
          .NET global tool for bootstrapping vsix &amp; pkg files. Just &quot;boots https://url/to/your/package&quot;!
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/jonathanpeppers/boots">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/jonathanpeppers">@jonathanpeppers</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/boots/">boots</a></code>
      </td>
    </tr>
    <tr>
      <td><code>bruce</code></td>
      <td>
        <p>
          A Command Line Kerberos .NET Management Tool.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/dotnet/kerberos.net">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://syfuhs.net/">@SteveSyfuhs</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/bruce/">bruce</a></code>
      </td>
    </tr>
    <tr>
      <td><code>certdump</code></td>
      <td>
        <p>
          CLI tool to dump the signing certificate from a Portable Executable (PE) file.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/secana/CertDump">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/secana">@secana</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/CertDump/">CertDump</a></code>
      </td>
    </tr>
    <tr>
      <td><code>certes</code></td>
      <td>
        <p>
          CLI tool for acquire certificates via the Automated Certificate Management Environment (ACME)
          protocol. (example: LetsEncrypt.org)
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/fszlin/certes">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/fszlin">@fszlin</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-certes/">dotnet-certes</a></code>
      </td>
    </tr>
    <tr>
      <td><code>cleanup</code></td>
      <td>
        <p>
          .NET Core Global Tool for cleaning up solution, project or folder.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/sebnilsson/DotnetCleanup">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/sebnilsson">@sebnilsson</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-cleanup/">dotnet-cleanup</a></code>
      </td>
    </tr>
    <tr>
      <td><code>codeconv</code></td>
      <td>
        <p>
          Codeconv converts code from VB.NET to C# (and vice versa)
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/icsharpcode/CodeConverter">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/icsharpcode/">@icsharpcode</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/ICSharpCode.CodeConverter.CodeConv/">ICSharpCode.CodeConverter.CodeConv</a></code>
      </td>
    </tr>
    <tr>
      <td><code>coverlet</code></td>
      <td>
        <p>
          Coverlet is a cross platform code coverage library for .NET Core, with support for line, branch and
          method coverage.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/tonerdo/coverlet">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/tonerdo">@tonerdo</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/coverlet.console/">coverlet.console</a></code>
      </td>
    </tr>
    <tr>
      <td><code>csmin</code></td>
      <td>
        <p>
          Fast and small utility to minify C# source. It removes whitespace and comments without
          altering the behaviour of the code. It is fast and small because it does not need or use Roslyn. It is
          <a href="https://www.nuget.org/packages/CSharpMinifier/">also available as a library</a>.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/atifaziz/CSharpMinifier">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/atifaziz">@atifaziz</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/CSharpMinifier/">CSharpMinifier</a></code>
      </td>
    </tr>
    <tr>
      <td><code>csval</code></td>
      <td>
        <p>
          Utility that validates a C# source for syntax errors.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/atifaziz/CSharpSyntaxValidator">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/atifaziz">@atifaziz</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/CSharpSyntaxValidator/">CSharpSyntaxValidator</a></code>
      </td>
    </tr>
    <tr>
      <td><code>CycloneDX</code></td>
      <td>
        <p>
          Creates CycloneDX Software Bill-of-Materials (SBOM) from .NET Projects
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/CycloneDX/cyclonedx-dotnet">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/stevespringett">@stevespringett</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/CycloneDX/">CycloneDX</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dacpac</code></td>
      <td>
        <p>
          Publish .dacpac on MS SQL Server without SSDT installed
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/GustavoAmerico/SQLServerDeploy/">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/GustavoAmerico">@gustavoamerico</a>
        </p>
        * Install
        <br />
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/Dacpac.Tool/">Dacpac.Tool</a></code>
        <br />
        * Run
        <br />
        <code> dotnet dacpac publish --dacpath=C:\artifact\db\ --server=mydatabase.server.contoso.com --databasenames='client1;client2;client3;client4' </code>
      </td>
    </tr>
    <tr>
      <td><code>dbtool</code></td>
      <td>
        <p>
          Exports database data to some commonly-used formats (XML, JSON, etc.) or imports the data in those formats back to DB.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/kedonec/Korzh.DbUtils">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/korzh">@korzh</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/Korzh.DbTool/">Korzh.DbTool</a></code>
      </td>
    </tr>
    <tr>
      <td><code>depguard</code></td>
      <td>
        <p>
          Check your projects for use of disallowed (blacklisted) NuGet packages, including transitive references.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/christophwille/dotnet-depguard/">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/christophwille/">@christophwille</a>
        </p>
        <code>dotnet tool install -g <a href="https://github.com/christophwille/dotnet-depguard/">depguard</a></code>
      </td>
    </tr>	
    <tr>
      <td><code>dmd5</code></td>
      <td>
        <p>
          Just generate MD5 hash value in CLI.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/Rwing/Dotnet.Tool.MD5">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/Rwing">@Rwing</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dmd5">dmd5</a></code>
      </td>
    </tr>
    <tr>
      <td><code>docker-watch</code></td>
      <td>
        <p>
          A command line utility to notify docker mounted volumes about changes on Windows.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/nickvdyck/docker-watch">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/nickvdyck">@nickvdyck</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/docker-watch">docker-watch</a></code>
      </td>
    </tr>
    <tr>
      <td><code>docs</code></td>
      <td>
        <p>
          Search <a href="https://docs.microsoft.com">docs.microsoft.com</a> using the command line.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/spboyer/dotnet-doc">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/spboyer">@spboyer</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-doc/">dotnet-doc</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-aop</code></td>
      <td>
        <p>
          A tool to make AOP for .cs files for your CI pipeline.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/ignatandrei/AOP_With_Roslyn">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/ignatandrei/">@ignatandrei</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-aop">dotnet-aop</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-apim</code></td>
      <td>
        <p>
          A cross-platform dotnet tool which streamlines the CI/CD process of deploying APIs into Azure API Management
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/mirsaeedi/dotnet-apim">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/mirsaeedi/">@mirsaeedi</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/Apim.DevOps.Toolkit/">Apim.DevOps.Toolkit</a></code>
      </td>
    </tr>	  
    <tr>
      <td><code>dotnet-aspnet-codegenerator</code></td>
      <td>
        <p>
          Code generation tool for creating controllers, views, and models in ASP.NET Core projects.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/aspnet/Scaffolding">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/aspnet">@aspnet</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-aspnet-codegenerator/">dotnet-aspnet-codegenerator</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-cake</code></td>
      <td>
        <p>
          A tool to run cross platform Cake build scripts.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/cake-build/cake">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/cake-build/">@cake-build</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/Cake.Tool/">Cake.Tool</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-combine</code></td>
      <td>
        <p>
          A tool that allows you to combine multiple C# source files into a single one, create a .zip with multiple files, etc.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/eduherminio/dotnet-combine">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/eduherminio">@eduherminio</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-combine/">dotnet-combine</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-config</code></td>
      <td>
        <p>
          A global tool for managing hierarchical configurations for dotnet tools, using git config format.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/kzu/dotnet-config">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/kzu/">@kzu</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-config/">dotnet-config</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-config2json</code></td>
      <td>
        <p>
          A simple tool to convert a web.config file to an appsettings.json file.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/andrewlock/dotnet-config2json">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/andrewlock/">@andrewlock</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-config2json/">dotnet-config2json</a></code>
      </td>
    </tr>
    <tr>
        <td><code>dotnet-coverageconverter</code></td>
        <td>
          <p>
            Convert `.coverage` files to `.coveragexml` files to support SonarCloud Code Coverage when using **VSTest@2**.
          </p>
          <p>
            <strong>Project site:</strong> <a href="https://github.com/StefH/CoverageConverter">GitHub</a>
            <br />
            <strong>Author:</strong> <a href="https://github.com/StefH">@StefH</a>
          </p>
          <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-coverageconverter/">dotnet-coverageconverter</a></code>
        </td>
    </tr>
    <tr>
      <td><code>dotnet-cowsay</code></td>
      <td>
        <p>
          CLI Tool that gives a a random blog post from discoverdot.net in cowsay format.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/isaac2004/dotnet-cowsay/">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/isaac2004">@isaac2004</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-cowsay/">dotnet-cowsay</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-cs2ts</code></td>
      <td>
        <p>
          Convert C# Models, ViewModels and DTOs into their TypeScript equivalents.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/AdrianWilczynski/CSharpToTypeScript">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/AdrianWilczynski">@AdrianWilczynski</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/CSharpToTypeScript.CLITool">CSharpToTypeScript.CLITool</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-dbinfo</code></td>
      <td>
        <p>
          A simple cross-platform command-line tool for get useful database information (in json format).
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/berkid89/dotnet-dbinfo">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/berkid89">@berkid89</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-dbinfo/">dotnet-dbinfo</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-depends</code></td>
      <td>
        <p>
          Dependency explorer for .NET.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/mholo65/depends">Github</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/mholo65">@mholo65</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-depends/">dotnet-depends</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-eb</code></td>
      <td>
        <p>
          Tools to deploy ASP.NET Core apps to AWS Elastic Beanstalk. Global tool started at version 3.0.0.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/aws/aws-extensions-for-dotnet-cli">Github</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/aws">@aws</a>
        </p>
        <code>dotnet tool install -g         <a href="https://www.nuget.org/packages/Amazon.ElasticBeanstalk.Tools/">Amazon.ElasticBeanstalk.Tools</a></code>
        <br />
      </td>
    </tr>
    <tr>
      <td><code>dotnet-ecs</code></td>
      <td>
        <p>
          Tools to deploy containers to Amazon Elastic Container Service functions. Global tool started at
          version 3.0.0.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/aws/aws-extensions-for-dotnet-cli">Github</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/aws">@aws</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/Amazon.ECS.Tools/">Amazon.ECS.Tools</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-encrypto</code></td>
      <td>
        <p> A tool to encrypt/decrypt folder or files using AES 256 Encryption Algorithm
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/tomchavakis/encrypto">Github</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/tomchavakis">@tomchavakis</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-encrypto">dotnet-encrypto</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-file</code></td>
      <td>
        <p>A dotnet global tool for downloading and updating loose files from arbitrary URLs.</p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/kzu/dotnet-file">Github</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/kzu">@kzu</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-file">dotnet-file</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-fm</code></td>
      <td>
        <p>
          FluentMigrator: Is a database migration framework for .NET much like Ruby on Rails Migrations.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://fluentmigrator.github.io/articles/runners/dotnet-fm.html">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/fluentmigrator">@FluentMigrator</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/FluentMigrator.DotNet.Cli/">FluentMigrator.DotNet.Cli</a></code>
      </td>
    </tr>
<tr>
    <td><code>dotnet-format</code></td>
    <td>
        <p>
            <code>dotnet-format</code> is a code formatter for <code>dotnet</code> that applies style preferences to a project or solution. Preferences will be read from an <code>.editorconfig</code> file, if present, otherwise a default set of preferences will be used.
        </p>
        <p>
            <strong>Project site:</strong> <a href="https://github.com/dotnet/format">GitHub</a>
            <br />
            <strong>Author:</strong> <a href="https://github.com/dotnet">@dotnet</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-format/">dotnet-format</a></code>
    </td>
</tr>
    <tr>
      <td><code>dotnet-fsharplint</code></td>
      <td>
        <p>
          Lint tool for F#.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/fsprojects/FSharpLint">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/fsprojects">@fsprojects</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-fsharplint/">dotnet-fsharplint</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-giio</code></td>
      <td>
        <p>
          A .NET global tool to create useful .gitignore files for your project using gitignore.io
        </p>
        <p>
          <strong>Author:</strong> <a href="https://github.com/liammoat">@liammoat</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-giio/">dotnet-giio</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-gitreleasemanager</code></td>
      <td>
        <p>
          Tool for creating and exporting releases for software applications hosted on Github </p>
        <p>
          <strong>Author:</strong> <a href="https://github.com/GitTools">@GitTools</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/GitReleaseManager.Tool">GitReleaseManager.Tool</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-gitversion</code></td>
      <td>
        <p>
          Easy Semantic Versioning (http://semver.org) for projects using Git.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/GitTools/GitVersion">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/GitTools">@GitTools</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/GitVersion.Tool">GitVersion.Tool</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-grab</code></td>
      <td>
        <p>
          .NET core global tool to download nuget packages in to a directory without any project. Useful when developing csx / fsx scripts
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/rohith/dotnet-grab">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/rohith">@rohith</a>
        </p>
        <code>dotnet tool install -g <a href="https://nuget.org/packages/dotnet-grab">dotnet-grab</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-hash</code></td>
      <td>
        <p>
          A simple dotnet tool to calculate hashes for the given file.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/TheBlueSky/dotnet-hash">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/TheBlueSky">@TheBlueSky</a>
        </p>
        <code>dotnet tool install -g         <a href="https://www.nuget.org/packages/TheBlueSky.DotNet.Tools.SwiftHash/">TheBlueSky.DotNet.Tools.SwiftHash</a></code>
        <br />
      </td>
    </tr>
    <tr>
      <td><code>dotnet-ignore</code></td>
      <td>
        <p>
          Global .NET Core tool that can download .gitignore file from github gitignore repository.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/Arasz/dotnet-ignore">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/Arasz">@Arasz</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-ignore/">dotnet-ignore</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-imgup</code></td>
      <td>
        <p>
          Global .NET Core tool to upload images on disk to <a href="https://imgur.com">imgur</a>.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/rohith/dotnet-imgup">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/rohith">@rohith</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-imgup/">dotnet-imgup</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-install</code></td>
      <td>
        <p>
          Provides capabilities for installing a .NET Core shared runtime.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/jaurenq/QB.DotNetCoreInstaller">Github</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/jaurenq">@jaurenq</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/QB.DotNetCoreInstaller/">QB.DotNetCoreInstaller</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-lambda</code></td>
      <td>
        <p>
          Tools to deploy AWS Lambda functions. Global tool started at version 3.0.0.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/aws/aws-extensions-for-dotnet-cli">Github</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/aws">@aws</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/Amazon.Lambda.Tools/">Amazon.Lambda.Tools</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-migrate-2017</code></td>
      <td>
        <p>
          Tool for converting a MSBuild project file (`csproj`) to VS2017 format and beyond.
        </p>
        <p>
          <strong>Author:</strong> <a href="https://github.com/hvanbakel">@hvanbakel</a>
        </p>
        <code>dotnet tool install -g         <a href="https://www.nuget.org/packages/Project2015To2017.Migrate2017.Tool">Project2015To2017.Migrate2017.Tool</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-namechk</code></td>
      <td>
        <p>
          Global .NET Core tool to check for the availability of package names on <a href="https://nuget.org">NuGet</a>
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/rohith/dotnet-namechk">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/rohith">@rohith</a>
        </p>
        <code>dotnet tool install -g <a href="https://nuget.org/packages/dotnet-namechk">dotnet-namechk</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-nuget-gc</code></td>
      <td>
        <p>
          A tool for cleaning the NuGet cache.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/terrajobst/dotnet-nuget-gc">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/terrajobst">@terrajobst</a>
        </p>
        <code>dotnet tool install -g <a href="https://nuget.org/packages/dotnet-nuget-gc">dotnet-nuget-gc</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-obfuscar</code></td>
      <td>
        <p>
          A .NET Core global tool to obfuscate assemblies.
        </p>
        <p>
	  <strong>Project site:</strong> <a href="https://github.com/obfuscar/obfuscar">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/lextm">@lextm</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/Obfuscar.GlobalTool/">Obfuscar.GlobalTool</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-octo</code></td>
      <td>
        <p>
          A .NET Core tool for octo.exe. This lets you install Octo onto a machine or build agent as long as you have the .NET Core 2.1.300 SDK available.
        </p>
        <p>
          <strong>Author:</strong> <a href="https://github.com/OctopusDeploy">@OctopusDeploy</a>
        </p>
	<p>
	Because it is common to install octo.exe in the cloud, you'll likely want to install it in a specific non-OS volume and on the version of Octopus Deploy you currently support:
	</p>
        <code>dotnet tool install <a href="https://www.nuget.org/packages/Octopus.DotNet.Cli/">Octopus.DotNet.Cli</a> --tool-path /path/for/tool --version &lt;version&gt;</code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-outdated</code></td>
      <td>
        <p>
          A .NET Core global tool to display and update outdated NuGet packages in a project.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/dotnet-outdated/dotnet-outdated">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/orgs/dotnet-outdated/people">dotnet-outdated team</a> & <a href="https://github.com/dotnet-outdated/dotnet-outdated/graphs/contributors">contributors</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-outdated-tool/">dotnet-outdated-tool</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-pr</code></td>
      <td>
        <p>
          .NET Core command-line (CLI) tool to open the browser in pull request mode for the code collaboration tool (GitHub, GitLab, Bitbucket++) connected to the current checked out branch (fetched via the git remote and/or tracking branch).
        </p>
        <p>
          <strong>Author:</strong> <a href="https://github.com/johnkors">@johnkors</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-pr">dotnet-pr</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-project-licenses</code></td>
      <td>
        <p>
          .NET Core tool to get the licenses of a project.
        </p>
        <p>
          <strong>Author:</strong> <a href="https://github.com/tomchavakis">@tomchavakis</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-project-licenses">dotnet-project-licenses</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-property</code></td>
      <td>
        <p>
          .NET Core command-line (CLI) tool to update project properties and version numbers on build.
        </p>
        <p>
          <strong>Author:</strong> <a href="https://github.com/loresoft">@pwelter34</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-property">dotnet-property</a></code>
      </td>
    </tr>
   <tr>
      <td><code>dotnet-readbin</code></td>
      <td>
        <p>
          A .NET Core global tool to convert encoded or serialized data to human-readable format. 
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/alphacloud/dotnet-readbin">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/alphacloud">@shatl</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-readbin">dotnet-readbin</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-references</code></td>
      <td>
        <p>
          Aids with bulk solution and project file references changes and related directory organisation. Particularly useful when used in docker builds to overcome COPY globbing limitations as described <a href="https://github.com/benmccallum/dotnet-references/blob/master/docs/Dockerfile-use-case.md">here</a>. 
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/benmccallum/dotnet-references">Github</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/benmccallum">@benmccallum</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-references/">dotnet-references</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-retire</code></td>
      <td>
        <p>
          A dotnet CLI extension to check your project for known vulnerabilities.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/retirenet/dotnet-retire">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/johnkors">@johnkors</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-retire">dotnet-retire</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-runas</code></td>
      <td>
        <p>
          Allows to run a dotnet process under a specified user account.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/JetBrains/runAs">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/NikolayPianikov">@NikolayPianikov</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-runas">dotnet-runas</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-script</code></td>
      <td>
        <p>
          Run C# scripts from the .NET CLI.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/filipw/dotnet-script">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/filipw">@filipw</a> <a href="https://github.com/seesharper">@seesharper</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-script/">dotnet-script</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-sdk</code></td>
      <td>
        <p>
          Manage .NET Core SDKs.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/jonstodle/DotNetSdkHelpers">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/jonstodle">@jonstodle</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/DotNetSdkHelpers/">DotNetSdkHelpers</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-search</code></td>
      <td>
        <p>
          Search for Nuget packages using the .NET Core CLI.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/billpratt/dotnet-search">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/billpratt">@billpratt</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-search/">dotnet-search</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-serve</code></td>
      <td>
        <p>
          A simple command line HTTP server, no code required.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/natemcmaster/dotnet-serve">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/natemcmaster">@natemcmaster</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-serve/">dotnet-serve</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-server</code></td>
      <td>
        <p>
          A configurable local http server to "mock" or fake responses from down stream services.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/joro550/dotnet-server">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/joro550">@joro550</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/DotNetSimpleServer/">DotNetSimpleServer</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-signtool</code></td>
      <td>
        <p>
          A tool for strong-name keys and signing of assemblies. 
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/AppCoreNet/SigningTool">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/AppCoreNet">@AppCoreNet</a>
        </p>
        <code>dotnet tool install --g <a href="https://www.nuget.org/packages/AppCore.SigningTool/">AppCore.SigningTool</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-snow</code></td>
      <td>
        <p>
          Avalonia-based cross-platform graphical snow demo.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/ptupitsyn/let-it-snow">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/ptupitsyn">@ptupitsyn</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-snow/">dotnet-snow</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-sonarscanner</code></td>
      <td>
        <p>
          The SonarScanner for MSBuild is the recommended way to launch a SonarQube or SonarCloud analysis
          for projects/solutions using dotnet command as build tool.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/SonarSource/sonar-scanner-msbuild">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/SonarSource">@SonarSource</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-sonarscanner">dotnet-sonarscanner</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-sort-refs</code></td>
      <td>
        <p>
          A tool to alphabetically sort package references in .NET projects. Also can be incluced in build pipeline to run checks.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/mysticmind/dotnet-sort-refs">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/mysticmind">@mysticmind</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-sort-refs">dotnet-sort-refs</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-sqldb</code></td>
      <td>
        <p>
          Using DbUp, to apply migration scripts etc. against a SQL-Server database.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/danielwertheim/dotnet-sqldb">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/danielwertheim">@danielwertheim</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-sqldb">dotnet-sqldb</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-sshdeploy</code></td>
      <td>
        <p>
          A dotnet CLI command that enables quick deployments over SSH.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/unosquare/sshdeploy">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/unosquare">@Unosquare</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-sshdeploy">dotnet-sshdeploy</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-symbol</code></td>
      <td>
        <p>
          Symbols download utility.
        </p>
        <p>
          <strong>Author:</strong> <a href="https://github.com/microsoft">@microsoft</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-symbol/">dotnet-symbol</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-thx</code></td>
      <td>
        <p>
          Find authors of packages you are using in you project and visit their GitHub.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/KrystianKolad/DotnetThx">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/KrystianKolad">@krystiankolad</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/DotnetThx">DotnetThx</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-toast</code></td>
      <td>
        <p>
          A .NET Core global tool to send custom toast notifications on Windows 10
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/rohith/dotnet-toast">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/rohith">@rohith</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-toast">dotnet-toast</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-tools-outdated</code></td>
      <td>
        <p>
          A .NET Global Tool to check whether any of currently installed global tools is outdated.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://dotnet.microsoft.com/platform/try-dotnet">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/rychlym">@rychlym</a>
        </p>
        <code>dotnet tool install --global <a href="https://www.nuget.org/packages/dotnet-tools-outdated/">dotnet-tools-outdated</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-try</code></td>
      <td>
        <p>
          Try.NET Global Tool: interactive in-browser documentation and workshop creator
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://dotnet.microsoft.com/platform/try-dotnet">Try .NET</a>
          <br />
          <strong>Source Code:</strong><a href="https://github.com/dotnet/try">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/dotnet">@dotnet (organization)</a>
        </p>
        <code>dotnet tool install --global <a href="https://www.nuget.org/packages/dotnet-try/">dotnet-try</a></code>
        <h3>Using dotnet-try</h3>
        <p>
          <code>git clone https://github.com/dotnet/try -b samples</code>
          <code>dotnet try</code>
        </p>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-updatealltools</code></td>
      <td>
        <p>
          The dotnet tool that can update all dotnet tools.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/dotnet-campus/dotnetCampus.UpdateAllDotNetTools">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/lindexi">@lindexi</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnetCampus.UpdateAllDotNetTools">dotnetCampus.UpdateAllDotNetTools</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-ups</code></td>
      <td>
        <p>
          Synchronize sln folder structure to physical folders also fixing project references.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/floatas/UPS">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/floatas">@Floatas</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-ups">dotnet-ups</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-version</code></td>
      <td>
        <p>
          A simple tool to update the version number of your project. If you know of yarn version, this is that for .NET.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/Jon-Indico/DotnetVersion">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/Jon-Indico">@Jon-Indico</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/DotnetVersion/">DotnetVersion</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnet-warp</code></td>
      <td>
        <p>
          A .NET Core global tool to pack project into single executable using Warp.
        </p>
        <p>
          <strong>Author:</strong> <a href="https://github.com/Hubert-Rybak">@Hubert-Rybak</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-warp/">dotnet-warp</a></code>
      </td>
    </tr>
    <tr>
        <td><code>dotnet-wiremock</code></td>
        <td>
          <p>
            WireMock.Net is a flexible library for stubbing and mocking web HTTP responses using request matching and response templating.
          </p>
          <p>
            <strong>Project site:</strong> <a href="https://github.com/WireMock-Net/WireMock.Net">GitHub</a>
            <br />
            <strong>Author:</strong> <a href="https://github.com/StefH">@StefH</a>
          </p>
          <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-wiremock/">dotnet-wiremock</a></code>
        </td>
      </tr>
    <tr>
      <td><code>dotnet-xdt</code></td>
      <td>
        <p>
          Toolbox for applying XML Document Transformations to .NET configuration files, or any other
          XML-structured content. Includes a .NET Core global tool, a .NET Standard library with no
          external dependencies, and a standalone .NET 4.6+ executable.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/nil4/dotnet-transform-xdt">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/nil4">@nil4</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-xdt/">dotnet-xdt</a></code>
      </td>
    </tr>
    <tr>
      <td><code>dotnetrsa</code></td>
      <td>
        <p>
          Generate rsa pkcs1, pkcs8, xml format key. Conversion between the three formats.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/stulzq/DotnetRSA">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/stulzq">@stulzq</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnetrsa">dotnetrsa</a></code>
      </td>
    </tr>
    <tr>
      <td><code>efg</code></td>
      <td>
        <p>
          .NET Core command-line (CLI) tool to generate Entity Framework Core model from an existing
          database.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/loresoft/EntityFrameworkCore.Generator">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/loresoft">@pwelter34</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/EntityFrameworkCore.Generator">EntityFrameworkCore.Generator</a></code>
      </td>
    </tr>
    <tr>
      <td><code>exceldna-unpack</code></td>
      <td>
        <p>
          Extract (unpack) the contents of Excel-DNA add-ins that have been packed with ExcelDnaPack, including .NET assemblies
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/augustoproiete/exceldna-unpack">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/augustoproiete">@augustoproiete</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/exceldna-unpack/">exceldna-unpack</a></code>
      </td>
    </tr>
    <tr>
      <td><code>execute</code></td>
      <td>
        <p>
          Console tool for running custom commands
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/ivanparvaresh/dotnet-exec">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/ivanparvaresh">@ivanparvaresh</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-tool-exec/">dotnet-tool-exec</a></code>
      </td>
    </tr>
    <tr>
      <td><code>fake</code></td>
      <td>
        <p>
          F# MAKE 5 - A DSL FOR BUILD TASKS AND MORE.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/fsharp/Fake">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/fsharp">@fsharp</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/fake-cli/">fake-cli</a></code>
      </td>
    </tr>
    <tr>
      <td><code>file-sort</code></td>
      <td>
        <p> A tool to organize files in folders based by date.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/thewindev/FileSort">Github</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/thewindev">@thewindev</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/file-sort/">file-sort</a></code>
      </td>
    </tr>
    <tr>
      <td><code>findref</code></td>
      <td>
        <p> Find which assemblies in a folder whom are referencing a given assembly
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/henrihs/findref">Github</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/henrihs">@henrihs</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/findref/">findref</a></code>
      </td>
    </tr>
    <tr>
      <td><code>flubu</code></td>
      <td>
        <p>
          Fluent Builder. A cross platform build automation tool for building projects and executing
          deployment
          scripts using C# code.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/flubu-core/flubu.core">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/flubu-core">@FlubuCore</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/FlubuCore.GlobalTool">FlubuCore.GlobalTool</a></code>
      </td>
    </tr>
    <tr>
      <td><code>ghi</code></td>
      <td>
        <p>
          A simple command-line client for managing GitHub Issues.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/jerriep/github-issues-cli">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/jerriep">@jerriep</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/github-issues-cli/">github-issues-cli</a></code>
      </td>
    </tr>
    <tr>
      <td><code>giphy</code></td>
      <td>
        <p>
          Find that giphy fast and just copy the url or markdown.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/DavidDeSloovere/giphy-cli">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/DavidDeSloovere">@DavidDeSloovere</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/GiphyCli/">GiphyCli</a></code>
      </td>
    </tr>
    <tr>
      <td><code>git-browse</code></td>
      <td>
        <p>
          Open the GitHub page or website for a repository in your browser.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/nickvdyck/git-browse">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/nickvdyck">@nickvdyck</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/git-browse">git-browse</a></code>
      </td>
    </tr>
    <tr>
      <td><code>git-flow-version</code></td>
      <td>
        <p>
          Create predictable and opinionated SemVer 2.0.0 version numbers for git flow repositories.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/hightechict/DashDashVersion">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/hightechict">@hightechict</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/git-flow-version">git-flow-version</a></code>
      </td>
    </tr>
    <tr>
      <td><code>git-istage</code></td>
      <td>
        <p> A better git add -p.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/terrajobst/git-istage">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/terrajobst">@terrajobst</a>
        </p>
        <code>dotnet tool install -g <a href="https://nuget.org/packages/git-istage">git-istage</a></code>
      </td>
    </tr>
    <tr>
      <td><code>git-rocket-filter</code></td>
      <td>
        <p>
          A powerful and faster version of git-filter-branch using C# Roslyn scripting to rewrite/filter commits.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/xoofx/git-rocket-filter">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/xoofx">@xoofx</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/git-rocket-filter/">git-rocket-filter</a></code>
      </td>
    </tr>
    <tr>
      <td><code>git-status</code></td>
      <td>
        <p>
          A simple command-line utility to determine status of all Git repositories in a directory structure.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/jerriep/git-status-cli">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/jerriep">@jerriep</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/git-status-cli/">git-status-cli</a></code>
      </td>
    </tr>
    <tr>
      <td><code>gitchanges</code></td>
      <td>
        <p>
          Generate changelogs from git history.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/bzumhagen/dotnet-gitchanges">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/bzumhagen">@bzumhagen</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-gitchanges">dotnet-gitchanges</a></code>
      </td>
    </tr>
    <tr>
      <td><code>gitcoauth</code></td>
      <td>
        <p>
          GitCoAuth: simple co-authorship commit line generator for Git commit messages.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/LorenzCK/github-coauth-tool">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/LorenzCK">@LorenzCK</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-gitcoauth">dotnet-gitcoauth</a></code>
      </td>
    </tr>
    <tr>
      <td><code>GitHubMarkdownSnippets</code></td>
      <td>
        <p>
          A utility for merging snippets into GitHub markdown document.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/SimonCropp/MarkdownSnippets#markdownsnippetstool">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/SimonCropp">@SimonCropp</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/MarkdownSnippets.Tool/">MarkdownSnippets.Tool</a></code>
      </td>
    </tr>
    <tr>
        <td><code>GitHubReleaseNotes</code></td>
        <td>
          <p>
            Generate Release Notes in markdown format from GitHub projects.
          </p>
          <p>
            <strong>Project site:</strong> <a href="https://github.com/StefH/GitHubReleaseNotes">GitHub</a>
            <br />
            <strong>Author:</strong> <a href="https://github.com/StefH">@StefH</a>
          </p>
          <code>dotnet tool install -g <a href="https://www.nuget.org/packages/GitHubReleaseNotes">GitHubReleaseNotes</a></code>
        </td>
    </tr>
    <tr>
      <td><code>gti</code></td>
      <td>
        <p>
          Global tool for installing .Net Global tools from a tools.gti file.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/shaun-h/gti">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/shaun-h">@shaun-h</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/gti/">gti</a></code>
      </td>
    </tr>
    <tr>
      <td><code>guid</code></td>
      <td>
        <p>
          .NET Core Global Tool for creating GUIDs/UUIDs.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/sebnilsson/DotnetGuid">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/sebnilsson">@sebnilsson</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-guid/">dotnet-guid</a></code>
      </td>
    </tr>
    <tr>
      <td><code>helveg</code></td>
      <td>
        <p>
          A software visualization tool. It turns projects into islands and classes into trees. It also sets the trees on fire if there are errors in them.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://gitlab.com/helveg/helveg">GitLab</a>
          <br />
          <strong>Author:</strong> <a href="https://gitlab.com/cafstep">@cafstep</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/helveg/">helveg</a></code>
      </td>
    </tr>
    <tr>
      <td><code>html-copy-vscode</code></td>
      <td>
        <p>
          A global tool to convert snippets copied from VS Code into plain html to paste into your blog.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/slang25/html-copy-vscode">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/slang25/">@slang25</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/HtmlCopyVSCode/">HtmlCopyVSCode</a></code>
      </td>
    </tr>
    <tr>
      <td><code>idgen</code></td>
      <td>
        <p>
          idgen supports the bulk generation of various types of unique identifiers.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/abock/idgen">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/abock">@abock</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/IdentifierGenerator/">IdentifierGenerator</a></code>
      </td>
    </tr>
    <tr>
      <td><code>ilspycmd</code></td>
      <td>
        <p>
          A tool for decompiling .NET assemblies and generating portable PDBs
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/icsharpcode/ILSpy/tree/master/ICSharpCode.Decompiler.Console">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/icsharpcode/ILSpy/">@ilspy</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/ilspycmd/">ilspycmd</a></code>
      </td>
    </tr>
    <tr>
      <td><code>installsdk</code></td>
      <td>
        <p>
            A global tool for downloading and installing .NET Core SDKs based on a global.json files.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/JosephWoodward/InstallSdkGlobalTool">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/JosephWoodward">@josephwoodward</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/InstallSdkGlobalTool/">InstallSdkGlobalTool</a></code>
      </td>
    </tr>
    <tr>
      <td><code>jitdasm</code></td>
      <td>
        <p>
          Disassembles one or more .NET methods / types to stdout or file(s). It can also create diffable disassembly.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/0xd4d/JitDasm">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/0xd4d">@0xd4d</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/JitDasm.0xd4d">JitDasm.0xd4d</a></code>
      </td>
    </tr>
    <tr>
      <td><code>json2yaml</code></td>
      <td>
        <p>
          A tool for converting json to yaml. Supports piping.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://gitlab.com/joostas/json-2-yaml">GitLab</a>
          <br />
          <strong>Author:</strong> <a href="https://gitlab.com/joostas">@joostas</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/json2yaml/">json2yaml</a></code>
      </td>
    </tr>	  
    <tr>
      <td><code>Kentico.Kontent.ModelGenerator</code></td>
      <td>
        <p>
          POCO model generator for Kentico Kontent.
        </p>
        <p>		
          <strong>Project site:</strong> <a href="https://github.com/Kentico/kontent-generators-net">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/kentico">@kentico</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/Kentico.Kontent.ModelGenerator/">Kentico.Kontent.ModelGenerator</a></code>
      </td>
    </tr>
    <tr>
      <td><code>kryptos</code></td>
      <td>
        <p>
          A .NET core tool for cryptography. Decode JWT tokens, generate file hashes with this cross platform CLI tool.
        </p>
        <p>		
          <strong>Project site:</strong> <a href="https://github.com/vijayshinva/kryptos">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/vijayshinva">@vijayshinva</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/Kryptos/">Kryptos</a></code>
      </td>
    </tr>     
    <tr>
      <td><code>kubedmc</code></td>
      <td>
        <p>
          Navigate into your favorite Kubernetes cluster with one finger!
        </p>
        <p>
          <strong>Author:</strong> <a href="https://github.com/Mimetis">@mimetis</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/KubeDmc/">kubedmc</a></code>
      </td>
    </tr>
    <tr>
      <td><code>libman</code></td>
      <td>
        <p>
          LibMan is a tool that helps you download common libraries from the Internet to use in your web
          project.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/aspnet/LibraryManager/wiki/Using-LibMan-CLI">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/aspnet">@aspnet</a>
        </p>
        <code>dotnet tool install -g         <a href="https://www.nuget.org/packages/Microsoft.Web.LibraryManager.CLI">Microsoft.Web.LibraryManager.CLI</a></code>
        <br />
      </td>
    </tr>
    <tr>
      <td><code>LiveReloadServer</code></td>
      <td>
        <p>
          A self-contained, generic, local Web Server that you can use to serve Web content from with optional support for Live Reload functionality for refreshing the site on content changes. Just point the tool at a folder and go. Also supports loose Razor Pages and has built-in Markdown document serving support.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/RickStrahl/Westwind.AspnetCore.LiveReload/tree/master/LiveReloadServer">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/rickstrahl">@rickstrahl</a>
        </p>
        <code>dotnet tool install -g         <a href="https://www.nuget.org/packages/LiveReloadServer/">LiveReloadServer</a></code>
        <br />
      </td>
    </tr>	  
    <tr>
      <td><code>LocalAppVeyor</code></td>
      <td>
        <p>
          .NET Core global tool which brings appveyor.yml to the center of your build process by making
          possible to execute its build jobs, locally.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/joaope/localappveyor">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/joaope">@joaope</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/localappveyor">localappveyor</a></code>
      </td>
    </tr>
    <tr>
      <td><code>mddox</code></td>
      <td>
        <p>
          A simple markdown documentation generator using reflection and XML comments.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/loxsmoke/mddox">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/loxsmoke">@loxsmoke</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/LoxSmoke.mddox">loxsmoke.mddox</a></code>
      </td>
    </tr>
    <tr>
      <td><code>minimig</code></td>
      <td>
        <p>
          A forward-only database migration tool.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/Jaxelr/Minimig">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/jaxelr">@jaxelr</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/minimig">minimig</a></code>
      </td>
    </tr>
    <tr>
      <td><code>minver-cli</code></td>
      <td>
        <p>
          A minimalistic command line tool for versioning any Git repository using tags.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/adamralph/minver">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/adamralph">@adamralph</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/minver-cli">minver-cli</a></code>
      </td>
    </tr>
    <tr>
      <td><code>moniker</code></td>
      <td>
        <p>
          Moniker CLI is a tiny .NET Core Global Tool for generating fun names. The names can follow the style used in Helm for release names or in Docker for container names.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/alexmg/Moniker">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/alexmg">@alexmg</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/Moniker.Cli/">moniker.cli</a></code>
      </td>
    </tr>
    <tr>
      <td><code>nanoff</code></td>
      <td>
        <p>
          A .NET Core Tool to update the firmware of nanoFramework devices. It can also backup the firmware, deployment and be used in production environment.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/nanoframework/nanoFirmwareFlasher">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/nanoframework">@AArnott</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/nanoFirmwareFlasher/">nanoFirmwareFlasher</a></code>
      </td>
    </tr>
    <tr>
      <td><code>nbgv</code></td>
      <td>
        <p>
          A .NET Core Tool that can install, read and set version information based on git history, using
          Nerdbank.GitVersioning.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/aarnott/Nerdbank.GitVersioning">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/AArnott">@AArnott</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/nbgv/">nbgv</a></code>
      </td>
    </tr>
    <tr>
      <td><code>ncbeauty</code></td>
      <td>
        <p>
          Move a .NET Core app runtime components and dependencies into a sub-directory and make it beauty.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/nulastudio/NetCoreBeauty">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/liesauer">@LiesAuer</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/nulastudio.ncbeauty/">nulastudio.ncbeauty</a></code>
      </td>
    </tr>
    <tr>
      <td><code>ndjson</code></td>
      <td>
        <p>
          A dotnet cli tool for printing newline delimited json to console.
        </p>
        <p>
          <strong>Author:</strong> <a href="https://github.com/fredeil">@fredeil</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/ndjson/">ndjson</a></code>
      </td>
    </tr>
    <tr>
      <td><code>nuget-deploy</code></td>
      <td>
        <p>
          Restore NuGet package if needed, and deploy it in a specified folder, by copying assemblies of the
          NuGet dependencies, or by generating appropriate `.deps.json` and `.runtimeconfig.json` files </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/stazz/NuGetUtils/tree/develop/Source/NuGetUtils.Tool.Deploy">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/stazz">@stazz</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/NuGetUtils.Tool.Deploy/">NuGetUtils.Tool.Deploy</a></code>
      </td>
    </tr>
    <tr>
      <td><code>nuget-exec</code></td>
      <td>
        <p>
          Restore NuGet package if needed, and execute a method within its assembly, loading dependencies as
          needed on-the-fly. Custom method parameter types are also supported.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/stazz/NuGetUtils/tree/develop/Source/NuGetUtils.Tool.Exec">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/stazz">@stazz</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/NuGetUtils.Tool.Exec/">NuGetUtils.Tool.Exec</a></code>
      </td>
    </tr>
    <tr>
      <td><code>nuget-restore</code></td>
      <td>
        <p>
          Restore one or more NuGet package, if needed.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/stazz/NuGetUtils/tree/develop/Source/NuGetUtils.Tool.Restore">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/stazz">@stazz</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/NuGetUtils.Tool.Restore/">NuGetUtils.Tool.Restore</a></code>
      </td>
    </tr>
    <tr>
      <td><code>NuGetKeyVaultSignTool</code></td>
      <td>
        <p>
          Code sign your .nupkg files using an Authenticode certificate stored in Azure Key Vault
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/onovotny/NuGetKeyVaultSignTool">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/onovotny">@onovotny</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/NuGetKeyVaultSignTool/">NuGetKeyVaultSignTool</a></code>
      </td>
    </tr>
    <tr>
      <td><code>nuke</code></td>
      <td>
        <p>
          Run and setup NUKE builds with a single command on any platform :rocket:
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/nuke-build/nuke">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/nuke-build">@nuke-build</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/Nuke.GlobalTool">Nuke.GlobalTool</a></code>
      </td>
    </tr>
    <tr>
      <td><code>NukedBit.NRepo</code></td>
      <td>
        <p>
          .NET Core Global Tool for simplifying repository creation with good defaults.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/nukedbit/nrepo">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/nukedbit">@nukedbit</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/NukedBit.NRepo">NukedBit.NRepo</a></code>
      </td>
    </tr>
    <tr>
      <td><code>NuKeeper</code></td>
      <td>
        <p>
          Find outdated NuGet packages and apply updates to them.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/NuKeeperDotNet/NuKeeper">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/anthonysteele">@AnthonySteele</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/NuKeeper">NuKeeper</a></code>
      </td>
    </tr>
    <tr>
      <td><code>nyancat</code></td>
      <td>
        <p>
          Nyancat 😻 in your terminal, rendered through ANSI escape sequences. A port of the original
          terminal application to make this cat run on dotnet core. 🐱‍🏍
        </p>
        <p>
          <strong>Author:</strong> <a href="https://github.com/nickvdyck">@nickvdyck</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/nyancat/">nyancat</a></code>
      </td>
    </tr>
    <tr>
      <td><code>omnia-cli</code></td>
      <td>
        <p>
          A cli tool for interacting with OMNIA Low-code REST API.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/omnialowcode/omnia-cli">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/omnialowcode/">@OMNIA Low-code</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/Omnia.CLI/">Omnia.CLI</a></code>
      </td>
    </tr>
    <tr>
      <td><code>orang</code></td>
      <td>
        <p>
          Search, replace, rename and delete directories, files and its content using the power of .NET regular expressions.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/josefpihrt/orang">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/josefpihrt">@JosefPihrt</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/orang.dotnet.cli">orang.dotnet.cli</a></code>
      </td>
    </tr>
    <tr>
      <td><code>otterkeys</code></td>
      <td>
        <p>
          Quickly create Ed25519 key pairs for signing and verifying messages or other data.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/miqo-no/OtterKeys">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/natsuo">@natsuo</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/OtterKeys">OtterKeys</a></code>
      </td>
    </tr>
    <tr>
      <td><code>p2u</code></td>
      <td>
        <p>
          Paste text content with Unix-like line terminations into Windows Terminal without extra line wrapping. Even into Cmd or Vim.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/celsojr/p2u">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/celsojr">@celsojr</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/p2u">p2u</a></code>
      </td>
    </tr>
    <tr>
      <td><code>pbm</code></td>
      <td>
        <p>
          <a href="https://cmd.petabridge.com/">Petabridge.Cmd CLI</a> for managing <a href="http://getakka.net/">Akka.NET</a>
          applications and clusters
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/petabridge/petabridge.cmd-issues">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://cmd.petabridge.com/">@petabridge</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/pbm/">pbm</a></code>
      </td>
    </tr>
    <tr>
      <td><code>protogen</code></td>
      <td>
        <p>
          protobuf-net code-generation from .proto schema files.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/mgravell/protobuf-net">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/mgravell">@mgravell</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/protobuf-net.Protogen/">protobuf-net.Protogen</a></code>
      </td>
    </tr>
    <tr>
      <td><code>pwsh</code></td>
      <td>
        <p>
          PowerShell Core global tool.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/PowerShell/PowerShell">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/PowerShell">@PowerShell</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/PowerShell/">PowerShell</a></code>
      </td>
    </tr>
    <tr>
      <td><code>recolor</code></td>
      <td>
        <p>
        Colors regex matches on STDIN lines
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/atifaziz/recolor">Github</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/atifaziz">@atifaziz</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/Recolor/">recolor</a></code>
      </td>
    </tr>
    <tr>
      <td><code>RendleLabs.NukeFromOrbit</code></td>
      <td>
        <p>
          Adds a `nuke-from-orbit` command that deletes all `bin` and `obj` directories from a solution, for times when it's the only way to be sure.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/RendleLabs/NukeFromOrbit/">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/markrendle">@markrendle</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/RendleLabs.NukeFromOrbit">RendleLabs.NukeFromOrbit</a></code>
      </td>
    </tr>
    <tr>
      <td><code>reportgenerator</code></td>
      <td>
        <p>
          ReportGenerator converts XML reports generated by OpenCover, PartCover, dotCover, Visual Studio,
          NCover or Cobertura into human readable reports in various formats.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/danielpalme/ReportGenerator/">GitHub</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-reportgenerator-globaltool">dotnet-reportgenerator-globaltool</a></code>
      </td>
    </tr>
    <tr>
      <td><code>rider</code></td>
      <td>
        <p>
          **Windows only** Adds a `rider` command to launch JetBrains Rider when it's installed via
          <a href="https://jetbrains.com/toolbox/">Toolbox</a>.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/RendleLabs/dotnet-rider-cli/">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/markrendle">@markrendle</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-rider-cli">dotnet-rider-cli</a></code>
      </td>
    </tr>
    <tr>
      <td><code>rimraf</code></td>
      <td>
        <p>
          rimraf as a .NET Core Global Tool.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/dotnet-tool/rimraf/">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/DoCode">@DoCode</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-rimraf">dotnet-rimraf</a></code>
      </td>
    </tr>
    <tr>
      <td><code>roslynator</code></td>
      <td>
        <p>
          A collection of 500+ analyzers, refactorings and fixes for C#, powered by Roslyn.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/JosefPihrt/Roslynator">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/JosefPihrt">@JosefPihrt</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/Roslynator.DotNet.Cli">roslynator.dotnet.cli</a></code>
      </td>
    </tr>
    <tr>
      <td><code>sbmgr</code></td>
      <td>
        <p>
          Azure servicebus message manager. List, send, resend and delete messages on servicebus queues or topics
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/thonhotels/message-manager">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://www.thonhotels.no">Thon Hotels</a> / <a href="https://novanet.no">Novanet</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/message-manager">message-manager</a></code>
      </td>
    </tr>
    <tr>
      <td><code>sharpfuzz</code></td>
      <td>
        <p>
          Command line tool for SharpFuzz instrumentation.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/Metalnem/sharpfuzz">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/Metalnem">@Metalnem</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/SharpFuzz.CommandLine/">SharpFuzz.CommandLine</a></code>
      </td>
    </tr>
    <tr>
      <td><code>skynet-cli</code></td>
      <td>
        <p>
          A command line tool for uploading files to Sia Skynet.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/drmathias/skynet-cli">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/drmathias">@drmathias</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/skynet-cli/">skynet-cli</a></code>
      </td>
    </tr>
    <tr>
      <td><code>sleet</code></td>
      <td>
        <p>
          A static NuGet feed generator.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/emgarten/Sleet">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/emgarten">@emgarten</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/Sleet/">Sleet</a></code>
      </td>
    </tr>
    <tr>
      <td><code>snitch</code></td>
      <td>
        <p>
          A tool that help you find transitive package references that can be removed.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/spectresystems/snitch">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/spectresystems">@Spectre Systems AB</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/Snitch/">Snitch</a></code>
      </td>
    </tr>
    <tr>
      <td><code>specsync</code></td>
      <td>
        <p>
          SpecSync for Azure DevOps is a synchronization tool that synchronizes BDD Gherkin feature files with Azure DevOps (TFS/VSTS).
        </p>
        <p>
          <strong>Author:</strong> <a href="https://github.com/gasparnagy">@gasparnagy</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/SpecSync.AzureDevOps">SpecSync.AzureDevOps</a></code>
      </td>
    </tr>
    <tr>
      <td><code>speech</code></td>
      <td>
        <p>
          Unofficial Azure Speech CLI - manage acoustic datasets, models, endpoints, transcriptions and more.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/msimecek/Azure-Speech-CLI">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/msimecek">@msimecek</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/azurespeechcli/">AzureSpeechCLI</a></code>
      </td>
    </tr>
    <tr>
      <td><code>srihash</code></td>
      <td>
        <p>
          Generates the SRI hash for <code>&lt;script&gt;</code> tags in browsers.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/natemcmaster/srihash-cli">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/natemcmaster">@natemcmaster</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/srihash-cli">srihash-cli</a></code>
      </td>
    </tr>
    <tr>
      <td><code>ssllabs-check</code></td>
      <td>
        <p>
          Tool that will check ssllabs score api and cert expiration when provided a list of hosts.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/ekonbenefits/dotnet-ssllabs-check">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/jbtule">@jbtule</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-ssllabs-check">dotnet-ssllabs-check</a></code>
      </td>
    </tr>
    <tr>
      <td><code>sysinfo</code></td>
      <td>
        <p>
          Outputs system information.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/markpflug/Elemental.SysInfoTool">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/markpflug">@markpflug</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/Elemental.SysInfoTool/">Elemental.SysInfoTool</a></code>
      </td>
    </tr>
    <tr>
      <td><code>t4</code></td>
      <td>
        <p>
          T4 text template processor.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/mono/t4">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/mhutch">@mhutch</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-t4/">dotnet-t4</a></code>
      </td>
    </tr>
    <tr>
      <td><code>tcpmux</code></td>
      <td>
        <p>
          TCP Multiplexer; provide simple routing of TCP traffic as well as SSL re-encryption and
          off-loading.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/nicodeslandes/TcpMux">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/nicodeslandes">@nicodeslandes</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/TcpMux/">TcpMux</a></code>
      </td>
    </tr>
    <tr>
      <td><code>templateversions</code></td>
      <td>
        <p>
          Lists all the versions of dotnet core SDKs in your user template directory and the global tools for each version.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/VictorioBerra/TemplateVersions.Tool">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/VictorioBerra">@VictorioBerra</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/TemplateVersions.Tool/">TemplateVersions.Tool</a></code>
      </td>
    </tr>
    <tr>
      <td><code>todo</code></td>
      <td>
        <p>
          The simple, powerfull and extensible Todo List app in your terminal.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/ivanpaulovich/todo">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/ivanpaulovich">@ivanpaulovich</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/todo">todo</a></code>
      </td>
    </tr>
    <tr>
      <td><code>trx2junit</code></td>
      <td>
        <p>
          Transforms XML from trx-Testresults to JUnit-Testresults / trx to JUnit XML.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/gfoidl/trx2junit">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/gfoidl">@gfoidl</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/trx2junit/">trx2junit</a></code>
      </td>
    </tr>
    <tr>
      <td><code>tus</code></td>
      <td>
        <p>
          A cli tool for interacting with a Tus enabled server.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/Jon-Indico/TusCli">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/Jon-Indico">@Jon-Indico</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/TusCli/">TusCli</a></code>
      </td>
    </tr>
    <tr>
      <td><code>unpkg</code></td>
      <td>
        <p>
          Front-end package manager that uses the <a href="https://unpkg.com">unpkg.com</a> CDN as a source.
          No Node.js, NPM or Bower required.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/RendleLabs/dotnet-unpkg">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/markrendle">@markrendle</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/RendleLabs.UnpkgCli">RendleLabs.UnpkgCli</a></code>
      </td>
    </tr>
    <tr>
      <td><code>upforgrabs</code></td>
      <td>
        <p>
          A tool to select a random .NET Open Source project/issue tagged with "up-for-grabs","firsttimer",
          etc.
          to work on.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/spboyer/dotnet-upforgrabs">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/spboyer">@spboyer</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/upforgrabs">upforgrabs</a></code>
      </td>
    </tr>
    <tr>
      <td><code>versioninfo</code></td>
      <td>
        <p>
          Display version information of .NET Core assemblies.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/taylorjg/dotnet-versioninfo">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/taylorjg">@taylorjg</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-versioninfo/">dotnet-versioninfo</a></code>
      </td>
    </tr>
    <tr>
      <td><code>vs</code></td>
      <td>
        <p>
          A global tool for managing Visual Studio installations.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/kzu/dotnet-vs">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/kzu/">@kzu</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-vs/">dotnet-vs</a></code>
      </td>
    </tr>
    <tr>
      <td><code>weather</code></td>
      <td>
        <p>
          Simple command-line tool for showing the current weather in your terminal
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/TheDayIsMyEnemy/WeatherCli">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/TheDayIsMyEnemy">@TheDayIsMyEnemy</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/weathercli/">weathercli</a></code>
      </td>
    </tr>	  
    <tr>
      <td><code>webtty</code></td>
      <td>
        <p>
          Simple command-line tool for sharing a terminal over the web.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/nickvdyck/webtty">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/nickvdyck">@nickvdyck</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/webtty/">webtty</a></code>
      </td>
    </tr>
    <tr>
      <td><code>weeknumber</code></td>
      <td>
        <p>
          Prints the current weeknumber to the command line.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/MarkusLund/weeknumber">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/MarkusLund">@MarkusLund</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/weeknumber/">weeknumber</a></code>
      </td>
    </tr>
    <tr>
      <td><code>WhiteSpaceWarrior</code></td>
      <td>
        <p>
           Removes all the stuff you get annoyed about when you speed-read code, such as empty lines, empty comments, and short meaningles comments.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/kbilsted/WhitespaceWarrior">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/kbilsted">@kbilsted</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/WhiteSpaceWarrior/">WhiteSpaceWarrior</a></code>
      </td>
    </tr>
    <tr>
      <td><code>xamarin-android-binderator</code></td>
      <td>
        <p>
          An engine to generate Xamarin Binding projects from Maven repositories with a JSON config and razor templates.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/Redth/Xamarin.AndroidBinderator">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/Redth">@Redth</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/Xamarin.AndroidBinderator.Tool/">Xamarin.AndroidBinderator.Tool</a></code>
      </td>
    </tr>
    <tr>
      <td><code>xscgen</code></td>
      <td>
        <p>
          Generate XmlSerializer compatible C# classes from XML Schema files.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/mganss/XmlSchemaClassGenerator">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/mganss">@mganss</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/dotnet-xscgen/">dotnet-xscgen</a></code>
      </td>
    </tr>
    <tr>
      <td><code>xstyler</code></td>
      <td>
        <p>
          CLI for XAML Styler. Format your XAML source code by integrating into build scripts, git commit templates, and more. This package is built on top of the same styling engine that powers the Visual Studio plugin.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/Xavalon/XamlStyler">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/Xavalon">Xavalon</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/XamlStyler.Console">XamlStyler.Console</a></code>
      </td>
    </tr>
    <tr>
      <td><code>xunit</code></td>
      <td>
        <p>
          Console tool for running xUnit.net tests
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/natemcmaster/xunit-cli">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/natemcmaster">@natemcmaster</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/xunit-cli">xunit-cli</a></code>
      </td>
    </tr>
    <tr>
      <td><code>yamlizr</code></td>
      <td>
        <p>
          Generate Azure Pipelines YAML and GitHub Actions YAML from Azure DevOps Classic Build/Release definitions.
        </p>
        <p>
          <strong>Project site:</strong> <a href="https://github.com/f2calv/yamlizr">GitHub</a>
          <br />
          <strong>Author:</strong> <a href="https://github.com/f2calv">@f2calv</a>
        </p>
        <code>dotnet tool install -g <a href="https://www.nuget.org/packages/yamlizr">yamlizr</a></code>
      </td>
    </tr>
  </tbody>
</table>

<!-- Contributors: when adding a new item to the list, please help me keep this list sorted by command name in alphabetical order. Thanks! -->
