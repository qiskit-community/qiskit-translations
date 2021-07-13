![Image](images/qiskit_header.png?raw=true)

> :warning: **This repository is not a package.**: The [setup.py](https://github.com/qiskit-community/qiskit-translations/blob/master/setup.py) file is only in this repository as a requirement for building docs. If you'd like to install Qiskit, follow the [link](https://github.com/Qiskit/qiskit).


# Qiskit Documentation Localization [![Crowdin](https://badges.crowdin.net/qiskit-docs/localized.svg)](https://crowdin.com/project/qiskit-docs)

First of all, **thank you** for showing your interest in translating (localizing) Qiskit Documentation! This helps make the documentation more accessible and available to our global community.

If you are interested in contributing to translations, please follow the instructions below.


### To sign up to participate in translations:

1. Open the [LOCALIZATION_CONTRIBUTORS](https://github.com/qiskit-community/qiskit-translations/blob/master/LOCALIZATION_CONTRIBUTORS) file. Look for the language header that you'd like to contribute to and sign up under there. If you do not find the language that you'd like to contribute to, please read [this section](#to-add-a-new-language-to-translate).<br/>
2. Create a pull request (PR) to add your name to the list. Make sure to follow the template to open a Pull Request.<br/>
      - Each contributor has to create their own PR and sign the CLA (see #3 below).
      - If you have an open issue for a language request, **add the issue link to the PR**.
   
   _(Not sure how to open a PR? Checkout [this section](#how-to-add-my-name-to-localization_contributors-list-and-open-a-pr-in-github))_

3. If you have not contributed to Qiskit before, you will be prompted to sign the Qiskit Contributors License Agreement (CLA) in your PR.<br/>
4. In the [Qiskit-Docs Crowdin project](https://crowdin.com/project/qiskit-docs), choose the language that you want to contribute to.<br/>
5. Click the **Join** button and **paste the URL of your PR** in the dialog box where you are asked why you want to join the Crowdin project.
![request_crowdin](images/image_send_request_in_crowdin.png?raw=true)
Failing to do so will result in a delay in approving your request in Crowdin and your Pull Request in GitHub. The administrators of the Crowdin project will review your request and give you access as quickly as they can.<br/>
6. For questions regarding onboarding or strategy, to connect with other translators and receive updates regarding the project please join #qiskit-localization channel in the [Qiskit workspace](http://ibm.co/joinqiskitslack) or make an issue in this repo.

### Project Leads

| Name | Slack ([Qiskit-Docs Workspace](http://bit.ly/qiskitdoc)) |
| ---    | --- |
| Yuri Kobayashi | @Yuri Kobayashi |
| Samanvay Sharma | @Samanvay Sharma |
| Soolu Thomas | @Soolu |


### Translation Leads (as of June, 2021)

| **Language** | **Translation Leads** | **Slack ([Qiskit Workspace](http://ibm.co/joinqiskitslack))** |
| ---     | ---    | --- |
| Bengali | Omar Shehab, Abhijit Mitra |  @Shehab @amitracal   |
| Chinese Simplified | Helena Zhang, Junye Huang |  @Helena Zhang @Junye   |
| Chinese Traditional | Helena Zhang, Junye Huang |  @Helena Zhang @Junye   |
| French | Olivier Hess | @Olivier Hess |
| German | Joachim Schaefer | @Joachim Schwarm |
| Greek | Vasilis Katopodis | @Vasilis Katopodis |
| Hindi | Samanvay Sharma | @sam |
| Hungarian | Andras Di Giovanni | @Andras Di Giovanni |
| Indonesian | Rudy Raymond, Eraraya Ricardo Muten | @rraymondhp @Eraraya Ricardo Muten |
| Italian | Eleonora Picca | @Eleonora Picca |
| Japanese | Takehiko Amano | @Takehiko Amano |
| Korean | Soyoung Shin, Saesun Kim | @Sophy @Saesun Kim |
| Malayalam | Ansah Mohammad Kuriyodath, Kiran Johns | @Ansah, @kiran |
| Polish | Piotr Biskupski | @pb.worker |
| Portuguese | Omar Costa Hamido | @OCH |
| Portuguese, Brazilian | Luiz Henrique Galeoti de Lima | @Luiz Galeoti |
| Russian | Artem Zasypalov, Vasily Shcherbinin | @artem.z @Vasily Shcherbinin |
| Spanish (United) | Carmen Recio Valcarce, Carlos Gonzalez | @carmenrv @Carlos Esteban Gonzalez |
| Swahili | Karoki Mugambi | @Karoki Mugambi |
| Tamil | Manjula Gandhi | @Manjula Gandhi |
| Turkish | Ayşin Sancı | @Ayshine |
| Urdu | Zia Mohammad | @Zia Mohammad |
| Vietnamese | Rossy Nhung Nguyen | @Rossy Ng |


### When you find an issue in the original documentation

During the process of translating Qiskit documentation, you may identify errors (mostly typos) in the original documentation. Please feel free to suggest corrections by opening an [issue](https://github.com/Qiskit/qiskit/issues/new/choose) and choose **Documentation**.


### What is Crowdin?

Qiskit documentation is translated (localized) using [Crowdin](https://crowdin.com/), a software and web localization platform that allows organizations to coordinate translation projects and collaborate with communities to translate materials. Crowdin allows our community of translators to amplify their impact by automatically reusing the work invested in translating one sentence, to translate other, similar sentences. Crowdin also makes translations resilient to many types of changes to the original material, such as moving sentences around, even across files.


### How to add a new language to translate?

The Qiskit Localization Project currently supports: Bengali, Chinese Simplified, Chinese Traditional, French, German, Greek, Hindi, Hungarian, Indonesian, Italian, Japanese, Korean, Malayalam, Polish, Portuguese, Russian, Spanish, Swahili, Tamil, Turkish, Urdu, and Vietnamese. These translations can be viewed from our [staging site](https://qiskit-community.github.io/qiskit-translations/).

[Japanese](https://qiskit.org/documentation/locale/ja_JP/index.html), [German](https://qiskit.org/documentation/locale/de_DE/index.html), [Korean](https://qiskit.org/documentation/locale/ko_KR/index.html), [Portuguese, Brazilian](https://qiskit.org/documentation/locale/pt_BR/index.html) and [French](https://qiskit.org/documentation/locale/fr_FR/index.html) documentation are now available in the [Qiskit Documentation website](https://qiskit.org/documentation/index.html).

As mentioned in the blog post [Qiskit in my language is Qiskit](https://medium.com/qiskit/qiskit-in-my-language-is-qiskit-73d4626a99d3), we want to make sure that translated languages have enough community support to ensure quality and consistency. <br/>

If you want to add a new language and become a translation lead, you can open a [GitHub issue](https://github.com/qiskit-community/qiskit-translations/issues/new/choose) to start a discussion with the Qiskit team and recruit translation project members. Please refer to the [criteria](#what-is-the-criteria-for-adding-a-new-language?) below to receive official support from the administrators for new languages.


### What is the criteria for adding a new language?

1. A minimum of **three contributors** is necessary for any new languages to be added and receive official support from the administrators of the localization project.<br/>
2. In addition to translators, we will need **dedicated proof-readers** to review the translations and approve accuracy of content in that language, to ensure the translations can be released in that language.<br/>
3. Among the group of contributors, a **translation lead must be identified** to serve as a liaison with the administrators of the localization project. The lead must contact Samanvay Sharma (samanvay.sharma1@ibm.com) and Yuri Kobayashi (yurik@jp.ibm.com) by email for the language to be officially listed under this project. <br/><br/>

These are general guidelines for joining translation efforts and adding new languages. If you have further questions, please feel free to contact [Samanvay Sharma](mailto:samanvay.sharma1@ibm.com?subject=[GitHub]%20Qiskit%20Documentation%20Translation) and [Yuri Kobayashi](mailto:yurik@jp.ibm.com?subject=[GitHub]%20Qiskit%20Documentation%20Translation). Thank you.


### How to add my name to LOCALIZATION_CONTRIBUTORS list and open a PR in GitHub?

**Option 1: In Github (Recommended)**
1. Click on the pen-like button which says "Edit this file" in the [LOCALIZATION_CONTRIBUTORS](https://github.com/qiskit-community/qiskit-translations/blob/master/LOCALIZATION_CONTRIBUTORS) file.
2. Add your name under the language you'd like to contribute to.
3. Once your name is added, scroll down and find a green button which says "Propose changes".
4. The page now reloads automatically and find and click on another green button - "Create pull request".
5. This should create the pull request and once that's done, follow the [instructions](https://github.com/qiskit-community/qiskit-translations/blob/master/README.md#to-sign-up-to-participate-in-translations) (step 3, 4, 5).

**Option 2: Creating a local clone of the repository and pushing from local**
1. Clone this repository by following [this guide](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository).
2. Make sure your local git configuration by following the instructions here -- [Setting username](https://docs.github.com/en/get-started/getting-started-with-git/setting-your-username-in-git) and [Setting email](https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/managing-email-preferences/setting-your-commit-email-address#setting-your-commit-email-address-in-git)
3. Create a branch by running `git checkout -b BRANCH_NAME` in your terminal.
4. Find LOCALIZATION_CONTRIBUTORS file in your local copy of qiskit-translations (created after cloning this repository) and add your name under the language you'd like to contribute to.
5. Now, in the terminal run `git add LOCALIZATION_CONTRIBUTORS`, `git commit -m "Added name under LANGUAGE-NAME"`, `git push origin BRANCH-NAME`. 
6. Follow the link in the terminal to open a pull request.
