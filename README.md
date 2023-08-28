![Image](images/qiskit_header.png?raw=true)

> :warning: **This repository is not a package.**: The [setup.py](https://github.com/qiskit-community/qiskit-translations/blob/main/setup.py) file is only in this repository as a requirement for building docs. If you'd like to install Qiskit, follow the [link](https://github.com/Qiskit/qiskit).

# Qiskit Documentation Localization [![Crowdin](https://badges.crowdin.net/qiskit-docs/localized.svg)](https://crowdin.com/project/qiskit-docs)

First of all, **thank you** for showing interest in translating (localizing) Qiskit Documentation! This helps make the documentation more accessible and available to our global community.

:eyes: **Please note that you must sign up separately if you want to join the localization project for [Qiskit Textbook](https://qiskit.org/learn/). For signing up to join the Qiskit Textbook Localization project, please refer the steps outlined [here](https://github.com/Qiskit/platypus/blob/main/TRANSLATING.md).**

If you are interested in contributing to Qiskit Documentation translations, please follow the instructions below.


## To sign up to participate in translations:

1. Open the [LOCALIZATION_CONTRIBUTORS](https://github.com/qiskit-community/qiskit-translations/blob/main/LOCALIZATION_CONTRIBUTORS) file. Look for the language header that you'd like to contribute to and sign up under there. If you do not find the language that you'd like to contribute to, please read [this section](#how-to-add-a-new-language-to-translate).<br/>
2. Create a pull request (PR) to add your name to the list. Make sure to follow the template to open a Pull Request.<br/>
      - Each contributor has to create their own PR and sign the CLA (see #3 below).
      - If you have an open issue for a language request, **add the issue link to the PR**.

   _(Not sure how to open a PR? Checkout [this section](#how-to-add-my-name-to-localization_contributors-list-and-open-a-pr-in-github))_

3. When you conribute to a Qiskit open source project on GitHub with a new pull request, a bot will evaluate whether you have signed the [Qiskit Contribution License Agreement (CLA)](https://qiskit.org/license/qiskit-cla.pdf). If it is your first time contributing to Qiskit, you will be prompted to sign the CLA in your PR. Please make sure to sign the CLA by accepting the agreement.
4. In the [Qiskit-Docs Crowdin project](https://crowdin.com/project/qiskit-docs), choose the language that you want to contribute to.<br/>
5. Click the **Join** button and **paste the URL of your PR** in the dialog box where you are asked why you want to join the Crowdin project.
![request_crowdin](images/image_send_request_in_crowdin.png?raw=true)
Failing to do so will result in a delay in approving your request in Crowdin and your Pull Request in GitHub. The administrators of the Crowdin project will review your request and give you access as quickly as they can.<br/>
6. For questions regarding onboarding or strategy, to connect with other translators and receive updates regarding the project please join #qiskit-localization channel in the [Qiskit workspace](http://ibm.co/joinqiskitslack) or make an issue in this repo.


## What is Crowdin?

Qiskit documentation is translated (localized) using [Crowdin](https://crowdin.com/), a software and web localization platform that allows organizations to coordinate translation projects and collaborate with communities to translate materials. Crowdin allows our community of translators to amplify their impact by automatically reusing the work invested in translating one sentence, to translate other, similar sentences. Crowdin also makes translations resilient to many types of changes to the original material, such as moving sentences around, even across files.


## How to add a new language to translate?

$$\color{#D22222}\textsf{\Large\&#x26A0;\kern{0.2cm}\Large We won't be adding any new languages to Crowdin until further notice.}$$

$$\color{#D22222}\textsf{\qquad\kern{0.2cm}\Large This is due to a lot of upcoming changes in the documentation.}$$

The list of languages that Qiskit Documentation Localization Project currently supports can be seen in the [Crowdin project page](https://crowdin.com/project/qiskit-docs).

As mentioned in the blog post [Qiskit in my language is Qiskit](https://medium.com/qiskit/qiskit-in-my-language-is-qiskit-73d4626a99d3), we want to make sure that translated languages have enough community support to ensure quality and consistency. <br/>

If you want to add a new language and become a translation lead, you can open a [GitHub issue](https://github.com/qiskit-community/qiskit-translations/issues/new/choose) to start a discussion with the Qiskit team and recruit translation project members. Please refer to the [criteria](#what-is-the-criteria-for-adding-a-new-language?) below to receive official support from the administrators for new languages.


## What is the criteria for adding a new language?

1. A minimum of **five contributors** is necessary for any new languages to be added and receive official support from the administrators of the localization project.<br/>
2. One of the contributors in that language must be a **Qiskit Advocate** and should actively participate.<br/>
3. In addition to translators, we will need **dedicated proof-readers** to review the translations and approve accuracy of content in that language and to ensure that the translations can be released in that language.<br/>
4. Among the group of contributors, a **translation lead must be identified** to serve as a liaison with the administrators of the localization project. The lead must contact [Soolu Thomas](mailto:soolu.thomas@ibm.com?subject=[GitHub]%20Qiskit%20Documentation%20Translation) and [Yuri Kobayashi](mailto:yurik@jp.ibm.com?subject=[GitHub]%20Qiskit%20Documentation%20Translation) by email containing the issue number (or link) and, a little intro about the TL(s) and the team after the above three criteria are met. <br/>
5. The project administrators will schedule a meeting with the translation lead(s) of the proposed language. Please note that satisfying the minimum number of translators does not automatically make the language ready to be added to Crowdin. It will be very important for the team to make continuous progress and to be active.

These are general guidelines for joining translation efforts and adding new languages. If you have further questions, please feel free to contact [Soolu Thomas](mailto:soolu.thomas@ibm.com?subject=[GitHub]%20Qiskit%20Documentation%20Translation) and [Yuri Kobayashi](mailto:yurik@jp.ibm.com?subject=[GitHub]%20Qiskit%20Documentation%20Translation). Thank you.


## How to add my name to LOCALIZATION_CONTRIBUTORS list and open a PR in GitHub?

**Option 1: In Github (Recommended)**
1. Click on the pen-like button which says "Edit this file" in the [LOCALIZATION_CONTRIBUTORS](https://github.com/qiskit-community/qiskit-translations/blob/main/LOCALIZATION_CONTRIBUTORS) file.
2. Add your name under the language you'd like to contribute to.
3. Once your name is added, scroll down and find a green button which says "Propose changes".
4. The page now reloads automatically and find and click on another green button - "Create pull request".
5. This should create the pull request and once that's done, follow the [instructions](https://github.com/qiskit-community/qiskit-translations/blob/main/README.md#to-sign-up-to-participate-in-translations) (step 3, 4, 5).

**Option 2: Creating a local clone of the repository and pushing from local**
1. Clone this repository by following [this guide](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository).
2. Make sure your local git configuration by following the instructions here -- [Setting username](https://docs.github.com/en/get-started/getting-started-with-git/setting-your-username-in-git) and [Setting email](https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/managing-email-preferences/setting-your-commit-email-address#setting-your-commit-email-address-in-git)
3. Create a branch by running `git checkout -b BRANCH_NAME` in your terminal.
4. Find LOCALIZATION_CONTRIBUTORS file in your local copy of qiskit-translations (created after cloning this repository) and add your name under the language you'd like to contribute to.
5. Now, in the terminal run `git add LOCALIZATION_CONTRIBUTORS`, `git commit -m "Added name under LANGUAGE-NAME"`, `git push origin BRANCH-NAME`.
6. Follow the link in the terminal to open a pull request.

## Digital Badges

At Qiskit, we feel that it is important to recognize the contributions that were made by its members to make our documentation more accessible to the global community. Starting in 2020, localization contributors who drove efforts in translating, proof-reading and managing progress can earn a Qiskit Localization Contributor Badge. For details, please refer to [Qiskit Localization Digital Badges](https://github.com/qiskit-community/qiskit-translations/blob/main/badges.md#qiskit-localization-digital-badges).

## When you find an issue in the original documentation

During the process of translating Qiskit documentation, you may identify errors (mostly typos) in the original documentation. Please feel free to suggest corrections by opening an [issue](https://github.com/Qiskit/qiskit/issues/new/choose) and choose **Documentation**.


## Project Leads

| Name | Slack ([Qiskit Workspace](http://ibm.co/joinqiskitslack)) |
| ---    | --- |
| Yuri Kobayashi | @Yuri Kobayashi |
| Sophy Shin | @Sophy |
| Soolu Thomas | @Soolu |
| Claudia Zendejas-Morales | @clausia |


## Translation Leads

| **Language** | **Translation Leads** | **Slack ([Qiskit Workspace](http://ibm.co/joinqiskitslack))** |
| ---     | ---    | --- |
| Bengali | Abhijit Mitra, Sristy Sangskriti |  @amitracal @Sristy Sangskriti  |
| Chinese Simplified | Helena Zhang, Wen-Sen Lu |  @Helena Zhang @Wen-Sen (Vince)  |
| Chinese Traditional | Helena Zhang, Wen-Sen Lu |  @Helena Zhang @Wen-Sen (Vince)  |
| French | Jean-Michel Torres | @torresjm |
| German | Thorsten Muehge | @Thorsten Mühge |
| Gujarati | Komal Pandya | @Komal Pandya |
| Hindi | Samanvay Sharma, Guncha Malik | @sam @Guncha Malik |
| Japanese | Takehiko Amano | @Takehiko Amano |
| Korean | Soyoung Shin, Mingi Ryu | @Sophy @Mingi|
| Marathi | Amol Deshmukh | @Amol Deshmukh |
| Polish | Piotr Biskupski | @pb.worker |
| Portuguese (United) | Luiz Henrique Galeoti de Lima, Omar Costa Hamido | @Luiz Galeoti @OCH |
| Russian | Vasily Shcherbinin, Farida Shagieva | @Vasily Shcherbinin @Farida |
| Spanish (United) | Claudia Zendejas-Morales, Rodrigo Rosado Rivial  | @clausia @rodrigo rosado |
| Tamil | Manjula Gandhi | @Manjula Gandhi |
| Telugu| Gayatri Vadaparty, Surya Sai Teja Desu | @Gayatri @Surya Sai Teja |
| Thai | Tanapat Deesuwan, Ruchipas Bavontaweepanya, Natchapol Patamawisut | @Tanapat @Ruchipas Bavontaweepanya @Bank Patamawisut |
| Turkish | Ayşin Sancı | @ayshine |

*(Last updated on May 31, 2023)*
