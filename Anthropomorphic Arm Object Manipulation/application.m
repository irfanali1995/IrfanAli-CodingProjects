function varargout = Application(varargin)
% APPLICATION MATLAB code for Application.fig
%      APPLICATION, by itself, creates a new APPLICATION or raises the existing
%      singleton*.
%
%      H = APPLICATION returns the handle to a new APPLICATION or the handle to
%      the existing singleton*.
%
%      APPLICATION('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in APPLICATION.M with the given input arguments.
%
%      APPLICATION('Property','Value',...) creates a new APPLICATION or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before Application_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to Application_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%

gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @Application_OpeningFcn, ...
                   'gui_OutputFcn',  @Application_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before Application is made visible.
function Application_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to Application (see VARARGIN)

% Choose default command line output for Application
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes Application wait for user response (see UIRESUME)
% uiwait(handles.figure1);
 [l1,l2,l3,l4,l5] = move_robot ([0 0 0 0 0]);
hold on;         
trimesh(l1,'FaceColor','r','EdgeColor','none');
trimesh(l2,'FaceColor','k','EdgeColor','none');
trimesh(l3,'FaceColor','r','EdgeColor','none');
trimesh(l4,'FaceColor','k','EdgeColor','none');
trimesh(l5,'FaceColor','r','EdgeColor','none');
view([45 45 45])
xlim([-400 400])
ylim([-400 400])
zlim([-100 700])
zlabel('z');
ylabel('y');
xlabel('x');

% --- Outputs from this function are returned to the command line.
function varargout = Application_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit1 as text
%        str2double(get(hObject,'String')) returns contents of edit1 as a double


% --- Executes during object creation, after setting all properties.
function edit1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit2_Callback(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit2 as text
%        str2double(get(hObject,'String')) returns contents of edit2 as a double


% --- Executes during object creation, after setting all properties.
function edit2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
Init_angles = [0 0 0 0 0 0]; %Initial position
pickup = str2num(char(get(handles.edit1,'String'))); %Pickup coordinates
drop = str2num(char(get(handles.edit2,'String'))); %Drop coordinates
PU_angles = InverseK (pickup, Init_angles); %Arrange of angles to pickup position
Dr_angles = InverseK (drop , PU_angles); %Arrange of angles to drop position
Tr1 = TrajectoryG (Init_angles, PU_angles);
Tr2 = TrajectoryG (PU_angles, Dr_angles);

for i=1:length(Tr1)
    cla();
    [l1,l2,l3,l4,l5] = move_robot ([Tr1(i,1), Tr1(i,2),Tr1(i,3),Tr1(i,4),Tr1(i,5)]);
    hold on;         
    trimesh(l1,'FaceColor','r','EdgeColor','none');
    trimesh(l2,'FaceColor','k','EdgeColor','none');
    trimesh(l3,'FaceColor','r','EdgeColor','none');
    trimesh(l4,'FaceColor','k','EdgeColor','none');
    trimesh(l5,'FaceColor','r','EdgeColor','none');
    view([45 45 45])
    xlim([-400 400])
    ylim([-400 400])
    zlim([-100 700])
    zlabel('z');
    ylabel('y');
    xlabel('x');
    pause(100/1000);
end

pause(1)

for i=1:length(Tr2)
    cla();
    [l1,l2,l3,l4,l5] = move_robot ([Tr2(i,1), Tr2(i,2),Tr2(i,3),Tr2(i,4),Tr2(i,5)]);
    hold on;         
    trimesh(l1,'FaceColor','r','EdgeColor','none');
    trimesh(l2,'FaceColor','k','EdgeColor','none');
    trimesh(l3,'FaceColor','r','EdgeColor','none');
    trimesh(l4,'FaceColor','k','EdgeColor','none');
    trimesh(l5,'FaceColor','r','EdgeColor','none');
    view([45 45 45])
    xlim([-400 400])
    ylim([-400 400])
    zlim([-100 700])
    zlabel('z');
    ylabel('y');
    xlabel('x');
    pause(100/1000);
end

% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
