#!/usr/bin/env zx
import fs from "fs";

const output = await $`cat package.json | grep name`;
console.log(output.stdout);

const branch = await $`git branch --show-current`;
console.log(branch.stdout);

await Promise.all([$`sleep 1; echo 1`, $`sleep 2; echo 2`, $`sleep 3; echo 3`]);

const name = "foo-bar";
const full_path = `/tmp/${name}`;
const is_already_present = fs.existsSync(full_path);

if (!is_already_present) {
  console.log("Directory is nonexistent, creating...");
  await $`mkdir /tmp/${name}`;
  console.log("Created...");
} else {
  console.log("Directory is already present, I will first delete it");
  const rm_output = await $`rm -rf ${full_path}`;
  console.log("Removed..., Now creating...");
  await $`mkdir /tmp/${name}`;
  console.log("Created...");
}
