const fs = require('fs');
const path = require('path');

function scaffold(yamlFilePath, targetBaseDir) {
  const content = fs.readFileSync(yamlFilePath, 'utf8');
  const lines = content.split(/\r?\n/);
  const stack = [{ indent: -1, dir: targetBaseDir }];

  for (let line of lines) {
    const trimmed = line.trimEnd();
    if (!trimmed) continue;

    const match = trimmed.match(/^(\s*)(.*)$/);
    if (!match) continue;

    const indent = match[1].length;
    const name = match[2];
    if (!name) continue;

    // Pop from stack until we find the parent with less indentation
    while (stack.length > 1 && stack[stack.length - 1].indent >= indent) {
      stack.pop();
    }

    const currentParent = stack[stack.length - 1].dir;
    const isDir = name.endsWith('/');
    const cleanName = isDir ? name.slice(0, -1) : name;
    const fullPath = path.join(currentParent, cleanName);

    if (isDir) {
      fs.mkdirSync(fullPath, { recursive: true });
      stack.push({ indent, dir: fullPath });
      console.log(`Created directory: ${fullPath}`);
    } else {
      fs.mkdirSync(path.dirname(fullPath), { recursive: true });
      if (!fs.existsSync(fullPath)) {
        fs.writeFileSync(fullPath, '', 'utf8');
        console.log(`Created file: ${fullPath}`);
      } else {
        console.log(`File already exists: ${fullPath}`);
      }
    }
  }
}

const args = process.argv.slice(2);
if (args.length < 1) {
  console.error("Usage: node scaffold-workspace.js <yaml-file-path> [target-base-dir]");
  process.exit(1);
}

const yamlFile = path.resolve(args[0]);
const baseDir = args[1] ? path.resolve(args[1]) : process.cwd();

scaffold(yamlFile, baseDir);
