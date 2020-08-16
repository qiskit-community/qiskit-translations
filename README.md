![Image](images/qiskit_header.png?raw=true)

> :warning: **This repository is not a package.**: The [setup.py](https://github.com/qiskit-community/qiskit-translations/blob/master/setup.py) file is only in this repository as a requirement for building docs. If you'd like to install Qiskit, follow the [link](https://github.com/Qiskit/qiskit).


# Qiskit Documentation Localization

First of all, **thank you** for showing your interest in translating (localizing) Qiskit Documentation! This helps make the documentation more accessible and available to our global community.

If you are interested in contributing to translations, please follow the instructions below.


### To sign up to participate in translations:

1. Open the [LOCALIZATION_CONTRIBUTORS](https://github.com/qiskit-community/qiskit-translations/blob/master/LOCALIZATION_CONTRIBUTORS) file. Look for the language header that you'd like to contribute to and sign up under there. If you do not find the language that you'd like to contribute to, please read [this section](#to-add-a-new-language-to-translate).<br/>
2. Create a pull request (PR) to add your name to the list. Make sure to follow the template to open a Pull Request.<br/>
      - Each contributor has to create their own PR and sign the CLA (see #3 below).
      - If you have an open issue for a language request, **add the issue link to the PR**.

3. If you have not contributed to Qiskit before, you will be prompted to sign the Qiskit Contributors License Agreement (CLA) in your PR.<br/>
4. In the [Qiskit-Docs Crowdin project](https://crowdin.com/project/qiskit-docs), choose the language that you want to contribute to.<br/>
5. Click the **Join** button and **paste the URL of your PR** in the dialog box where you are asked why you want to join the Crowdin project.
![request_crowdin](images/image_send_request_in_crowdin.png?raw=true)
Failing to do so will result in a delay in approving your request in Crowdin and your Pull Request in GitHub. The administrators of the Crowdin project will review your request and give you access as quickly as they can.<br/>
6. For questions regarding onboarding or strategy, to connect with other translators and receive updates regarding the project please join #qiskit-localization channel in the [Qiskit workspace](http://ibm.co/joinqiskitslack) or make an issue in this repo.

### Project Leads (as of Aug, 2020)

| Role | Name | Slack ([Qiskit Workspace](http://ibm.co/joinqiskitslack)) |
| ---     | ---    | --- |
| Qiskit Localization Lead | Yuri Kobayashi | @Yuri Kobayashi |
| Qiskit Localization Technical Lead | Soolu Thomas | @Soolu |


### Translation Leads (as of Aug, 2020)

| Language | Translation Leads | Slack ([Qiskit Workspace](http://ibm.co/joinqiskitslack)) |
| ---     | ---    | --- |
| Brazilian Portuguese | Jose Gilberto Biondo Junior | @Gilberto Biondo |
| Hindi | Anupama Ray | @anupamar |
| French | Olivier Hess | @Olivier Hess |
| German | Joachim Schaefer | @Joachim Schwarm |
| Indonesian | Rudy Raymond, Eraraya Ricardo Muten | @rraymondhp @Eraraya Ricardo Muten |
| Italian | Eleonora Picca | @Eleonora Picca |
| Japanese | Takehiko Amano | @Takehiko Amano |
| Korean | Jinho Hwang | @Jinho Hwang |
| Polish | Piotr Biskupski | @pb.worker |
| Portuguese | Omar Costa Hamido | @OCH |
| Spanish | Arturo Acuaviva Huertos, Enric Delgado Samper | @Arturo Acuaviva |
| Spanish-Mexico | Carlos Gonzalez | @Carlos Esteban Gonzalez |
| Turkish | Ayşin Taşdelen | @Ayshine |


### When you find an issue in the original documentation

During the process of translating Qiskit documentation, you may identify errors (mostly typos) in the original documentation. Please feel free to suggest corrections by opening an [issue](https://github.com/Qiskit/qiskit/issues/new/choose) and choose **Documentation**.


### What is Crowdin?

Qiskit documentation is translated (localized) using [Crowdin](https://crowdin.com/), a software and web localization platform that allows organizations to coordinate translation projects and collaborate with communities to translate materials. Crowdin allows our community of translators to amplify their impact by automatically reusing the work invested in translating one sentence, to translate other, similar sentences. Crowdin also makes translations resilient to many types of changes to the original material, such as moving sentences around, even across files.


### How to add a new language to translate?

The Qiskit Localization Project currently supports: Brazilian Portuguese, French, German, Italian, Japanese, Korean, Polish, Portuguese, Spanish, Spanish- Mexico, and Turkish. These translations can be viewed from our [staging site](https://qiskit-community.github.io/qiskit-translations/).

[Japanese](https://qiskit.org/documentation/locale/ja_JP/index.html), [German](https://qiskit.org/documentation/locale/de_DE/index.html) and [Korean](https://qiskit.org/documentation/locale/ko_KR/index.html) documentation are now available in the [Qiskit Documentation website](https://qiskit.org/documentation/index.html).

As mentioned in the blog post [Qiskit in my language is Qiskit](https://medium.com/qiskit/qiskit-in-my-language-is-qiskit-73d4626a99d3), we want to make sure that translated languages have enough community support to ensure quality and consistency. <br/>

If you want to add a new language and become a translation lead, you can open a [GitHub issue](https://github.com/qiskit-community/qiskit-translations/issues/new/choose) to start a discussion with the Qiskit team and recruit translation project members. Please refer to the [criteria](#what-is-the-criteria-for-adding-a-new-language?) below to receive official support from the administrators for new languages.


### What is the criteria for adding a new language?

1. A minimum of **three contributors** is necessary for any new languages to be added and receive official support from the administrators of the localization project.<br/>
2. In addition to translators, we will need **dedicated proof-readers** to review the translations and approve accuracy of content in that language, to ensure the translations can be released in that language.<br/>
3. Among the group of contributors, a **translation lead must be identified** to serve as a liaison with the administrators of the localization project. The lead must contact Yuri Kobayashi (yurik@jp.ibm.com) by email for the language to be officially listed under this project. <br/><br/>

These are general guidelines for joining translation efforts and adding new languages. If you have further questions, please feel free to contact [Yuri Kobayashi](mailto:yurik@jp.ibm.com?subject=[GitHub]%20Qiskit%20Documentation%20Translation). Thank you.
