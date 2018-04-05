
function helloworld()
  %output hello world
  disp('hello world.');
  
  %call function
  b()
  
  %save workspace
  save hello
  
  %load workspace
  load hello
end

function b()
  %output a + b
  a = 1;
  b = 3;
  disp(a+b)
  disp(pi)
end
