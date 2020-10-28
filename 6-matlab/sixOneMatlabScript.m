data = importdata("data.txt")';
scale = importdata("scale.txt")';

dV = scale(1);
dt = scale(2);

U = data * dV;
t = (1:length(data)) * dt;

[m, i] = max(data);

tCharge = i * dt;
tDischarge = (length(data) - i) * dt;

f1 = figure();
plot(t, U, '-o', 'Color', [0,0.7,0.9], 'MarkerIndices',1:20:length(U), 'LineWidth', 2, 'MarkerSize', 5);
grid on;
title({'����������� ����������', '�� ������������ � RC �������', '�� �������'});
xlabel("�����, �");
ylabel("����������, �");
legend('U(t)', 'Location', 'northeast');

text(max(t) * 0.6, max(U) * 0.6, ['����� ������ = ' num2str(tCharge) ' c'], 'BackgroundColor', 'w');
text(max(t) * 0.6, max(U) * 0.5, ['����� ������� = ' num2str(tDischarge) ' c'], 'BackgroundColor', 'w');

saveas(f1, "cap.png");
saveas(f1, "cap.svg");