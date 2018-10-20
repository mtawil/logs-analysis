# Logs Analysis

This project has been developed in response to the newspaper request to analyse their articles and authors based on logs.

## Getting Started

These instructions will help you out to run this code on your local machine.

### Prerequisites

1. Download and install [Vagrant 2.2.0](https://releases.hashicorp.com/vagrant/2.2.0/)
2. Download Vagrantfile and install the virtual box:
```sh
$ git clone https://github.com/udacity/fullstack-nanodegree-vm.git FSND_VM
$ cd FSND_VM/vagrant
$ vagrant up
```
> Depends on your internet speed, the `vagrant up` command will take a few minutes, be patient :)

3. Download the database file, unzip it, then delete the unneeded zip file:

```sh
$ curl -L https://github.com/mtawil/logs-analysis/files/2498083/newsdata.zip > newsdata.zip
$ unzip newsdata.zip && rm -f newsdata.zip
```

> Make sure that you've downloaded it on the same vagrant directory so that it can be accessible inside the virtual box.

### Installing

1. First of all, let's log into the virtual box using `vagrant ssh`, after that, go to the shared directory inside the virtual box `cd /vagrant`.
2. Clone this repo into the shared directory:

```sh
$ git clone https://github.com/mtawil/logs-analysis.git /vagrant/logs-analysis
```

> Please make sure you're on the shared directory and all the listed files as below are presented:
>
> <img src="https://user-images.githubusercontent.com/700753/47255461-33812380-d47a-11e8-8485-6ae57e932a5b.png" width="458" height="112">

3. Import the database:

```sh
psql -d news -f newsdata.sql
```

4. Install the project requirements:

```sh
$ pip3 install -r requirements.txt
```

The output you get should be like this:

<img src="https://user-images.githubusercontent.com/700753/47215551-7f649780-d3aa-11e8-8f92-4a1892d1749c.png" width="470" height="129">


## Running and analysis the logs

After you successfully installations, you can run this code by:
```sh
$ python3 main.py
```

The output results should be like the below screenshot

<img src="https://user-images.githubusercontent.com/700753/47215552-7ffd2e00-d3aa-11e8-8fb2-042906afdac1.png" width="430" height="197">

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

This project use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/mtawil/logs-analysis/tags). 

## Authors

* **Mohammad AlTaweel** - *Initial work* - [mtawil](https://github.com/mtawil)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
