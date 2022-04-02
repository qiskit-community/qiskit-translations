![Image](images/qiskit-logo-purple.png?raw=true)

> :warning: **This repository is not a package.**: The [setup.py](https://github.com/qiskit-community/qiskit-translations/blob/master/setup.py) file is only in this repository as a requirement for building docs. If you'd like to install Qiskit, follow the [link](https://github.com/Qiskit/qiskit).


# Qiskit Textbook Localization

First of all, **thank you** for showing interest in translating (localizing) Qiskit Textbook! This helps make the textbook more accessible and available to our global community.

If you are interested in contributing to translations, please follow the instructions below.</br>
**Please note that localization_contributors of Qiskit Documentation must sign up for this project separately and complete the steps below to join the Qiskit Textbook Localization project.**


## Steps to participate in Qiskit textbook translations:

1. Open the [TEXTBOOK_CONTRIBUTORS](https://github.com/qiskit-community/qiskit-translations/TEXTBOOK_CONTRIBUTORS) file. Look for the language header that you'd like to contribute to and add your full name under he header. If you do not find the language that you'd like to contribute to, please read [this section](#how-to-add-a-new-language).<br/>
2. Create a pull request (PR) to add your name to the list. Make sure to follow the template to open a PR.<br/>
Each contributor must create their own PR and sign the Contributors License Agreement (CLA). (see #3 below).
If you have an open issue for a language request, **add the issue link to the PR**.

   _(Not sure how to open a PR? Checkout [this section](#how-to-add-my-name-to-textbook_contributors-list-and-open-a-pr-in-github))_
   
3. When you conribute to a Qiskit open source project on GitHub with a new pull request, a bot will evaluate whether you have signed the [Qiksit Contribution License Agreement (CLA)](https://qiskit.org/license/qiskit-cla.pdf). If it is your first time contributing to Qiskit, you will be prompted to sign the CLA in your PR. Please make sure to sign the CLA by accepting the agreement.<br/>
4. Join [GitLocalize](https://gitlocalize.com) using the same GitHub ID you used to open your PR above.  
5. Once your PR has been accepted and merged, you will receive a notfication from GitLocalize with a title: [GitLocalize]You have been assined a new role.<br/>
6. Join project [Qiskit/platypus] and then visit the language you signed up to contribute to.<br/>
7. For questions about the project, to connect with other translators, or to receive updates regarding the project, please join #qiskit-localization channel in the [Qiskit workspace](http://ibm.co/joinqiskitslack). <br/>

## Review the CLA document
The [Qiksit Contribution License Agreement (CLA)](https://qiskit.org/license/qiskit-cla.pdf) document is available for review as PDF.

## What is GitLocalize?

[GitLocalize](https://gitlocalize.com) is a platform for managing translations of the content stored on GitHub and simplifies the translation workflow for developers.

Important note:<br/>
Gitlocalize is under active development, so you may encounter issues during translation. If you find bugs or errors, please feel free to reach out to translation leads or open an issue [here](https://github.com/gitlocalize/gitlocalize-ibm/issues). 


## How to add a new language?

The Qiskit Localization Project currently supports: Bengali, Chinese Simplified, Chinese Traditional, French, German, Greek, Hindi, Hungarian, Indonesian, Italian, Japanese, Korean, Malayalam, Marathi, Polish, Portuguese, Russian, Spanish, Swahili, Tamil, Thai, Turkish, Urdu, and Vietnamese. 

If you want to add a new language and become a translation lead, you can open a [GitHub issue](https://github.com/qiskit-community/qiskit-translations/issues/new/choose) to start a discussion with the Qiskit team and recruit translation project members. Please refer to the [criteria](#what-is-the-criteria-for-adding-a-new-language?) below to receive official support from the administrators for new languages.


## What is the criteria for adding a new language?

1. A minimum of **three contributors** is necessary for any new language to be added and receive official support from the administrators of the Qiskit Textbook localization project.<br/>
2. In addition to translators, we will need **dedicated proof-readers** to review the translations and approve accuracy of content in that language, to ensure the translations can be released in that language.<br/>
3. Among the group of contributors, a **translation lead must be identified** to serve as a liaison with the administrators of the localization project. The lead must contact [Soolu Thomas](mailto:soolu.thomas@ibm.com?subject=[GitHub]%20Qiskit%20Documentation%20Translation) and [Yuri Kobayashi](mailto:yurik@jp.ibm.com?subject=[GitHub]%20Qiskit%20Documentation%20Translation) by email for the language to be officially listed under this project. <br/>

These are general guidelines for joining translation efforts and adding new languages. If you have further questions, please feel free to contact [Soolu Thomas](mailto:soolu.thomas@ibm.com?subject=[GitHub]%20Qiskit%20Documentation%20Translation) and [Yuri Kobayashi](mailto:yurik@jp.ibm.com?subject=[GitHub]%20Qiskit%20Documentation%20Translation). Thank you.


## How to add my name to TEXTBOOK_CONTRIBUTORS list and open a PR in GitHub?

**Option 1: In Github (Recommended)**
1. Click on the pen-like button which says "Edit this file" in the [TEXTBOOK_CONTRIBUTORS](https://github.com/qiskit-community/qiskit-translations/blob/master/TEXTBOOK_CONTRIBUTORS) file.
2. Add your name under the language you'd like to contribute to.
3. Once your name is added, scroll down and find a green button which says "Propose changes".
4. The page now reloads automatically and find and click on another green button - "Create pull request".
5. This should create the pull request and once that's done, follow the [instructions](https://github.com/qiskit-community/qiskit-translations/blob/master/TEXTBOOK_README.md#steps-to-participate-in-qiskit-textbook-translations) (steps 3, 4, 5, 6).

**Option 2: Creating a local clone of the repository and pushing from local**
1. Clone this repository by following [this guide](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository).
2. Make sure your local git configuration by following the instructions here -- [Setting username](https://docs.github.com/en/get-started/getting-started-with-git/setting-your-username-in-git) and [Setting email](https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/managing-email-preferences/setting-your-commit-email-address#setting-your-commit-email-address-in-git)
3. Create a branch by running `git checkout -b BRANCH_NAME` in your terminal.
4. Find TEXTBOOK_CONTRIBUTORS file in your local copy of qiskit-translations (created after cloning this repository) and add your name under the language you'd like to contribute to.
5. Now, in the terminal run `git add TEXTBOOK_CONTRIBUTORS`, `git commit -m "Added name under LANGUAGE-NAME"`, `git push origin BRANCH-NAME`. 
6. Follow the link in the terminal to open a pull request.


## When you find an issue in the textbook

During the process of translating Qiskit Textbook (beta), you may identify bug or errors regarding the original textbook content. Please feel free to suggest corrections by opening an [issue](https://github.com/Qiskit/platypus/issues/new/choose).

## Project Leads

| Name | Slack ([Qiskit Workspace](http://ibm.co/joinqiskitslack)) |
| ---    | --- |
| Yuri Kobayashi | @Yuri Kobayashi |
| Soolu Thomas | @Soolu |s


## Translation Leads (as of April 2022)

| **Language** | **Translation Leads** | **Slack ([Qiskit Workspace](http://ibm.co/joinqiskitslack))** |
| ---     | ---    | --- |
| Bengali | Abhijit Mitra, Sristy Sangskriti, Omar Shehab |  @amitracal @Sristy Sangskriti @Shehab  |
| Chinese Simplified | Helena Zhang, Wen-Sen Lu |  @Helena Zhang @Wen-Sen (Vince)  |
| Chinese Traditional | Helena Zhang, Wen-Sen Lu |  @Helena Zhang @Wen-Sen (Vince)  |
| French | Jean-Michel Torres | @torresjm |
| German | Thorsten Muehge | @Thorsten Mühge |
| Greek | Vasilis Katopodis | @Vasilis Katopodis |
| Hindi | Samanvay Sharma, Guncha Malik | @sam @Guncha Malik |
| Hungarian | Andras Di Giovanni | @Andras Di Giovanni |
| Indonesian | Rudy Raymond, Eraraya Ricardo Muten | @rraymondhp @Eraraya Ricardo Muten |
| Italian | Eleonora Picca | @Eleonora Picca |
| Japanese | Kifumi Numata, Takehiko Amano |@Kifumi Numata @Takehiko Amano |
| Korean | Soyoung Shin, Mingi Ryu | @Sophy @Mingi|
| Malayalam | Ansah Mohammad Kuriyodath | @Ansah |
| Marathi | Amol Deshmukh | @Amol Deshmukh |
| Polish | Piotr Biskupski | @pb.worker |
| Portuguese (United) | Luiz Henrique Galeoti de Lima, Omar Costa Hamido | @Luiz Galeoti @OCH |
| Russian | Artem Zasypalov, Vasily Shcherbinin, Farida Shagieva | @artem.z @Vasily Shcherbinin @Farida |
| Spanish (United) | Claudia Zendejas-Morales, Rodrigo Rosado Rivial  | @clausia @rodrigo rosado |
| Swahili | Karoki Mugambi | @Karoki Mugambi |
| Tamil | Manjula Gandhi | @Manjula Gandhi |
| Thai | Tanapat Deesuwan, Ruchipas Bavontaweepanya, Natchapol Patamawisut | @Tanapat @Ruchipas Bavontaweepanya @Bank Patamawisut |
| Turkish | Ayşin Sancı, Furkan Semih Dündar | @ayshine @Furkan Semih Dündar |
| Urdu | Zia Mohammad | @Zia Mohammad |
| Vietnamese | Rossy Nhung Nguyen | @Rossy Ng |
