var express = require('express');
var router = express.Router();

const util = require('util');
const fs = require('fs');
const exec = util.promisify(require('child_process').exec);
const child_process = require("child_process");

async function run(cmd) {
  const { stdout, stderr } = await exec(cmd);
}

const takeScreen = async function() {
    let time = new Date().getTime()
    let cmd = `adb shell screencap -p /sdcard/tmp.png &&
    adb pull /sdcard/tmp.png public/images/current-${time}.png &&
    cp public/images/current-${time}.png public/images/current.png &&
    cp public/images/current-${time}.png screen/current-${time}.png
    `
    await run(cmd)
    return `images/current-${time}.png`
}

const jumpAction = function(time=100) {
    let cmd = `adb shell input swipe 100 100 100 100 ${time}`
    run(cmd)
}

const logger = function (logFile, data) {
    let writeStream = fs.createWriteStream(logFile, {
        flags: 'a'
    })
    writeStream.write(data, 'utf-8')
    writeStream.on('finish', () => {
        console.log('write log file over.')
    })
    writeStream.end()
}

/* GET home page. */
router.get('/', function (req, res, next) {
    res.render('jump', {
        title: 'Express'
    });
});

router.post('/', async function (req, res, next) {
    let { distance, time } = req.body
    console.log(distance, time)
    if(time < 0) {
        time = 0
    }
    logger('output.txt', `${distance},${time}\n`)
    jumpAction(time)
    child_process.execSync("sleep 3");
    let imagePath =  await takeScreen()
    res.json({
        msg: 'ok',
        image: imagePath
    });
});

module.exports = router;